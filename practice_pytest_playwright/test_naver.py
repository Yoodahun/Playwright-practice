import re

from playwright.sync_api import Page, expect


class TestNaver:

    def test_naver_home(self, page:Page):

        page.goto("http://www.naver.com", wait_until="load")
        expect(page.locator("a").filter(has_text=re.compile(r"^NAVER$"))).to_be_visible()