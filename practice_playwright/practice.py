from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.get_by_label("로그인").click()

    page.get_by_role("button", name="계정 만들기").click()
    # page.get_by_role("menuitem", name="개인용").click()
    page.get_by_label("성(선택사항)").fill("Playwright")
    page.get_by_label("성(선택사항)").press("Tab")
    page.get_by_label("이름").fill("testing")
    page.get_by_role("button", name="다음").click()
    page.get_by_label("연").click()
    page.get_by_label("연").fill("1991")
    # page.get_by_label("연").press("Tab")
    page.get_by_label("월").select_option("1")
    # page.get_by_label("월").press("Tab")
    page.get_by_label("일").fill("7")
    # page.get_by_label("일").press("Tab")
    page.get_by_label("성별", exact=True).select_option("남자")
    page.get_by_role("button", name="다음").click()
    page.get_by_label("내 Gmail 주소 만들기").click()
    page.get_by_label("Gmail 주소 만들기", exact=True).fill("testing.playwright232")
    page.get_by_role("button", name="다음").click()

    element = page.get_by_text('안전한 비밀번호 만들기', exact=True)
    expect(element).to_contain_text("비밀번호")
    expect(element).to_be_visible(visible=False)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
