from selene import browser, be, have
import pytest

@pytest.fixture()
def browser_open_full_window():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

@pytest.fixture()
def browser_duckduckgo(browser_open_full_window):
    browser.open("https://duckduckgo.com/")

    yield

    browser.quit()

@pytest.fixture()
def browser_yandex(browser_open_full_window):
    browser.open("https://ya.ru")

    yield

    browser.quit()