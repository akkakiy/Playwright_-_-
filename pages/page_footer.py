import allure

from locators.locators_book import BookLocators
from pages.base_page import BasePage


@allure.suite('Footer')
class PageFooter(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @allure.step('Поиск текста "О КнигиРум"')
    def find_text_book_room(self):
        return self.page.get_by_text(BookLocators.BOOK_ROOM).сlick()

    @allure.step('Поиск текста "Партнерам по доставке"')
    def find_and_click_text_delivery(self):
        return self.page.get_by_text(BookLocators.DELIVERY).click()

    @allure.step('Поиск текста "Условия работы с партнерами по доставке"')
    def find_text_delivery(self):
        return self.page.get_by_role("heading", name="Условия работы с партнерами по доставке")

    @allure.step('Поиск текста "Партнерам-селерам"')
    def find_and_click_text_selers(self):
        return self.page.get_by_text(BookLocators.SELERS).click()

    @allure.step('Поиск текста "Условия работы для партнеров - селлеров"')
    def find_text_selers(self):
        return self.page.get_by_role("heading", name="Условия работы для партнеров - селлеров")

    @allure.step('Поиск текста "Помощь"')
    def find_and_click_text_help(self):
        return self.page.get_by_text(BookLocators.HELP).click()

    @allure.step('Поиск текста "Помощь"')
    def find_text_help(self):
        return self.page.get_by_role("heading", name="Помощь")

    @allure.step('Поиск текста "Цены"')  # пока не знаю как проверить
    def find_and_click_text_price(self):
        return self.page.get_by_role("link", name="Цены").click()

    @allure.step('Поиск текста "FAQs"')
    def find_and_click_text_faq(self):
        return self.page.get_by_text(BookLocators.FAQ).click()

    @allure.step('Поиск текста "Каковы условия доставки и возврата товаров?"')
    def find_text_faq(self):
        return self.page.get_by_text("Каковы условия доставки и возврата товаров?")
