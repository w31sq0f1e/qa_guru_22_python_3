from selene import browser, be, have
import pytest

def test_browser_search(browser_yandex):
    browser.element('[name="text"]').should(be.blank).type('fdsfgfgdfacx').press_enter()
    browser.element('.Distribution-ButtonClose').should(be.clickable).click()
    browser.element('[class="EmptySearchResults-Title"]').should(have.text('Ничего не нашли'))