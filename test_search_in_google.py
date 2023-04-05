from faker import Faker
from selene.support.shared import browser
from selene import be, have


def test_google_search_selene_results_shown(init_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_search_random_string_no_results(init_browser):
    fake = Faker()
    random_string = fake.pystr(20)
    browser.element('[name="q"]').should(be.blank).type(random_string).press_enter()
    browser.element('#result-stats').should(have.text('Результатов: примерно 0'))
