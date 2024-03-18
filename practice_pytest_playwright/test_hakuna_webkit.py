import time

from playwright.sync_api import Page, expect, Browser, BrowserContext

class TestHakunaWebkit():

    def test_hakuna_webkit(self, build_trace_viewer_file_dir, page: Page, context: BrowserContext):
        javascript = """
        const getMockVideoStreamTrack = function(width = 100, height = 100) {
          const canvas = document.createElement('canvas');
          canvas.width = width;
          canvas.height = height;
          const context = canvas.getContext('2d');

          setInterval(() => {
            if (context) {
              context.clearRect(0, 0, width, height);

              const imageData = context.createImageData(width, height);
              const pixels = imageData.data;
              const numPixels = imageData.width * imageData.height;

              for (let i = 0; i < numPixels; i += 1) {
                pixels[i * 4] = Math.floor(Math.random() * 255); 
                pixels[i * 4 + 1] = Math.floor(Math.random() * 255); 
                pixels[i * 4 + 2] = Math.floor(Math.random() * 255);
                pixels[i * 4 + 3] = 255; // Alpha
              }

              context.putImageData(imageData, 0, 0);
            }
          }, 500);

          const stream = canvas.captureStream();
          const videoTrack = stream.getVideoTracks()[0];
          return videoTrack;
        };

        const getMockAudioStreamTrack = function() {
          const context = new AudioContext();
          const destination = context.createMediaStreamDestination();

          const gain = context.createGain();
          gain.gain.value = 0;
          gain.connect(destination);

          const osc = context.createOscillator();
          osc.connect(gain);
          osc.start();

          let nextMusicNoteIndex = 0;

          setInterval(() => {
            const { currentTime } = context;
            osc.frequency.value = littleStarNotes[nextMusicNoteIndex];
            gain.gain.setValueAtTime(0.5, currentTime);
            gain.gain.exponentialRampToValueAtTime(
              0.00001, currentTime + 0.5,
            );

            if (nextMusicNoteIndex >= littleStarNotes.length - 1) {
              nextMusicNoteIndex = 0;
            } else {
              nextMusicNoteIndex += 1;
            }
          }, 1000);

          const audioTrack = destination.stream.getAudioTracks()[0];
          return audioTrack;
        };

        const NOTES = {
          C: 1047,
          D: 1175,
          E: 1319,
          F: 1397,
          G: 1568,
          A: 1760,
        };


        const littleStarNotes = [
          NOTES.C,
          NOTES.C,
          NOTES.G,
          NOTES.G
        ];

        if (true) {
          let enumerateDevices = [];
          navigator.mediaDevices.getUserMedia = (constraints) => {
            enumerateDevices = [];
            const tracks = [];
            if (constraints?.audio) {
              const audioTrack = getMockAudioStreamTrack();
              tracks.push(audioTrack);
              enumerateDevices.push({
                label: audioTrack.label,
                kind: 'audioinput',
                groupId: '1',
                deviceId: '1',
                toJSON: () => '',
              });
            }
            if (constraints?.video) {
              const videoTrack = getMockVideoStreamTrack();
              tracks.push(videoTrack);
              enumerateDevices.push({
                label: videoTrack.label,
                kind: 'videoinput',
                groupId: '2',
                deviceId: '2',
                toJSON: () => '',
              });
            }

            const stream = new MediaStream(tracks);
            return Promise.resolve(stream);
          };
          navigator.mediaDevices.enumerateDevices = async () => enumerateDevices;
        }
        """

        page.goto("https://webrtc.github.io/samples/src/content/getusermedia/gum/")

        # time.sleep(2)
        page.evaluate(javascript)
        page.get_by_text("Open camera").click()
        page.evaluate(javascript)
        # page.get_by_role("button", name="Test my cam").click()
        time.sleep(10)
