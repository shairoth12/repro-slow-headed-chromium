from playwright.sync_api import Page, expect


def test_bbc(page: Page):
    """
    Some basic navigations and scrolling on the BBC website,
    to highlight the slow performance of the headed browser.
    """

    page.goto("https://www.bbc.com")
    open_menu_button = page.get_by_role("button", name="Open menu")
    open_menu_button.click()

    nav_to_sport = page.get_by_test_id("level0NavText-/sport")
    with page.expect_navigation():
        nav_to_sport.click()

    footer = page.get_by_test_id("footer-content")
    footer.scroll_into_view_if_needed()
    nav_to_terms_of_use_from_footer = footer.get_by_text("Terms of Use")
    expect(nav_to_terms_of_use_from_footer).to_be_visible()
    with page.expect_navigation():
        nav_to_terms_of_use_from_footer.click()

    expect(
        page.get_by_role("heading", name="A few rules for us and you", level=1)
    ).to_be_visible()

    explore_bbc_heading = page.get_by_role("heading", name="Explore the BBC", level=2)
    explore_bbc_heading.scroll_into_view_if_needed()
    explore_bbc_heading.hover()
    expect(explore_bbc_heading).to_be_visible()

    page.goto("https://www.bbc.com")
    open_menu_button.click()
    expect(nav_to_sport).to_be_visible()
