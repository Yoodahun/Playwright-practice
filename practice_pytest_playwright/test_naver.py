import re
import pytest

from playwright.sync_api import Page, expect


class TestNaver:

    def test_naver_home(self, page:Page):

        page.goto("http://www.naver.com", wait_until="load")
        # assert page.locator("a").filter(has_text=re.compile(r"^NAVER$")).is_visible()
        page.evaluate('''async () => {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            const videoTrack = stream.getVideoTracks()[0];
            console.log('Using video device: ' + videoTrack.label);
        }''')

        page.pause()

        # expect(page.locator("a").filter(has_text=re.compile(r"^NAVER$"))).to_be_visible()

    def test_naver_home_with_fail(self, page:Page):

        page.goto("http://www.naver.com", wait_until="load")
        # assert page.locator("a").filter(has_text=re.compile(r"^NAVER$")).is_visible()

        expect(page.locator("a").filter(has_text=re.compile(r"^NAVER$"))).to_be_visible()

    def test_naver_home_with_success(self, page:Page):

        page.goto("http://www.naver.com", wait_until="load")
        # assert page.locator("a").filter(has_text=re.compile(r"^NAVER$")).is_visible()

        expect(page.locator("a").filter(has_text=re.compile(r"^NAVER$"))).to_be_hidden()