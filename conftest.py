from typing import Generator

from playwright.sync_api import Browser, Page
import pytest


@pytest.fixture(scope="function")
def new_page(
    browser: Browser,
) -> Generator[Page, None, None]:
    browser_context = browser.new_context(
        permissions=["clipboard-read", "clipboard-write"],
    )

    return browser_context.new_page()
