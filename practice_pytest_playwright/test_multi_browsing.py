import time

from playwright.sync_api import Page, expect, Browser, BrowserContext


class TestMultiBrowsing():

    def test_multi_browsing(self, build_trace_viewer_file_dir, page: Page, context: BrowserContext):
        page.goto("http://www.naver.com", wait_until="load")
        page.get_by_placeholder("검색어를 입력해 주세요").fill("Test1")
        page.get_by_role("button", name="검색", exact=True).click()

        expect(page.get_by_role("link", name="NAVER", exact=True)).to_be_visible()

        another_browser = context.browser.new_context()

        another_page = another_browser.new_page()

        try:
            another_page.goto("http://www.naver.com", wait_until="load")
            another_page.get_by_placeholder("검색어를 입력해 주세요").fill("Test1234")
            another_page.get_by_role("button", name="검색", exact=True).click()
            time.sleep(2)
            expect(another_page.get_by_role("link", name="NAVER", exact=True)).to_be_visible()

        finally:

            another_page.close()
            another_browser.close()

    def test_multi_browsing2(self, browser:Browser, page: Page):
        page.goto("http://www.naver.com", wait_until="load")
        page.get_by_placeholder("검색어를 입력해 주세요").fill("Test1")
        page.get_by_role("button", name="검색", exact=True).click()

        expect(page.get_by_role("link", name="NAVER", exact=True)).to_be_visible()

        another_context = browser.new_context()
        # another_context.tracing.start(screenshots=True, snapshots=True, sources=True)
        another_page = another_context.new_page()

        # try:
        another_page.goto("http://www.naver.com", wait_until="load")
        another_page.get_by_placeholder("검색어를 입력해 주세요").fill("Test5678")
        another_page.get_by_role("button", name="검색", exact=True).click()
        time.sleep(2)
        expect(another_page.get_by_role("link", name="NAVER", exact=True)).to_be_visible()

        # another_context.tracing.stop(path="trace2.zip")

        another_page.close()
        another_context.close()

    # def test_multi_context(self, page: Page, context: BrowserContext):
    #     page.goto("http://www.naver.com", wait_until="load")
    #     page.get_by_role("link", name="NAVER 로그인").click()
    #     page.get_by_placeholder("아이디").click()
    #     page.get_by_placeholder("아이디").fill("tty4032")
    #     page.get_by_placeholder("아이디").press("Tab")
    #     page.get_by_placeholder("비밀번호").fill("Wnrdmffo1!")
    #     page.get_by_role("button", name="로그인").click()
    #     time.sleep(2)
    #     page.context.storage_state(path="playwright/.auth/login.json")
    #
    #     context.clear_cookies()
    #     another_page = context.new_page()
    #     another_page.goto("https://www.naver.com")

