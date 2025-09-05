from selene import browser, be, have
import pytest

def test_browser_search(browser_duckduckgo):
    browser.element('[name="q"]').should(be.blank).type('qa.guru').press_enter()
    browser.element('html').should(have.text('Автоматизация тестирования на Python - qa.guru'))