from selene.support.shared import browser
from selene import be, have


def test_google_search_positive(open_browser):
    positive_search: str = 'selene'
    positive_search_result: str = 'yashaka/selene: User-oriented Web UI browser tests in Python'

    browser.element('[name="q"]').should(be.blank).type(positive_search).press_enter()
    browser.element('[id="search"]').should(have.text(positive_search_result))


def test_google_search_negative(open_browser):
    negative_search: str = 'efjoaerghuitgiubviIER'
    negative_search_result: str = 'Your search - efjoaerghuitgiubviIER - did not match any documents.'

    browser.element('[name="q"]').should(be.blank).type(negative_search).press_enter()
    browser.element('[id="rcnt"]').should(have.text(negative_search_result))
