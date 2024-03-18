function getMockVideoStreamTrack() {
  const canvas = document.createElement("canvas")
  canvas.width = 100
  canvas.height = 100
  const context = canvas.getContext("2d")

  setInterval(() => {
    if (context) {
      context.clearRect(0, 0, 100, 100)

      const imageData = context.createImageData(100, 100)
      const pixels = imageData.data
      const numPixels = imageData.width * imageData.height

      for (let i = 0; i < numPixels; i += 1) {
        pixels[i * 4] = Math.floor(Math.random() * 255) // R
        pixels[i * 4 + 1] = Math.floor(Math.random() * 255) // G
        pixels[i * 4 + 2] = Math.floor(Math.random() * 255) // B
        pixels[i * 4 + 3] = 255 // Alpha
      }

      context.putImageData(imageData, 0, 0)
    }
  }, 500)

  const stream = canvas.captureStream()
  const videoTrack = stream.getVideoTracks()[0]
  return videoTrack
}

let enumerateDevices = []
navigator.mediaDevices.getUserMedia = constraints => {
  enumerateDevices = []
  const tracks = []

  if (constraints?.video) {
    const videoTrack = getMockVideoStreamTrack()
    tracks.push(videoTrack)
    enumerateDevices.push({
      label: videoTrack.label,
      kind: "videoinput",
      groupId: "2",
      deviceId: "2",
      toJSON: () => ""
    })
  }

  const stream = new MediaStream(tracks)
  return Promise.resolve(stream)
}

navigator.mediaDevices.enumerateDevices = async () => enumerateDevices
