import allure

from locators.locators_book import BookLocators
from pages.base_page import BasePage


class PageLocatorsBookRoom(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @allure.step('Поиск и клик по кнопке "Каталог"')
    def find_and_click_catalog(self):
        return self.page.get_by_text(BookLocators.TEXT_CATALOG).click()

    @allure.step('Поиск поля "Поиск по каталогу"')
    def find_placeholder(self):
        return self.page.get_by_placeholder(BookLocators.TEXT_PLACEHOLDER)

    @allure.step('Поиск и заполнение поля "Поиск по каталогу"')
    def find_and_fill_placeholder(self):
        return self.page.get_by_placeholder(BookLocators.TEXT_PLACEHOLDER).fill('Ловец снов')

    @allure.step('Поиск и заполнение поля "Поиск по каталогу" по имени и фамилии автора')
    def find_and_fill_placeholder_name_and_lastname_author(self):
        return self.page.get_by_placeholder(BookLocators.TEXT_PLACEHOLDER).fill('Говард Лавкрафт')

    @allure.step('Поиск и заполнение поля "Поиск по каталогу" по имени автора')
    def find_and_fill_placeholder_name_author(self):
        return self.page.get_by_placeholder(BookLocators.TEXT_PLACEHOLDER).fill('Говард')

    @allure.step('Поиск и заполнение поля "Поиск по каталогу" по фамилии автора')
    def find_and_fill_placeholder_lastname_author(self):
        return self.page.get_by_placeholder(BookLocators.TEXT_PLACEHOLDER).fill('Лавкрафт')

    @allure.step('Поиск и клик по кнопке "Поиск"')
    def find_and_click_search_btn(self):
        return self.page.locator(BookLocators.SEARCH_BTN).click()

    @allure.step('Поиск и клик по книге "Ловец снов"')
    def find_and_click_book(self):
        return self.page.get_by_text(BookLocators.NAME_BOOK_KING).click()

    @allure.step('Поиск картинки "Ловец снов"')
    def find_img_book(self):
        return self.page.get_by_alt_text(BookLocators.IMG_BOOK)

    @allure.step('Поиск по названия книги')
    def find_name_book(self):
        return self.page.get_by_text(BookLocators.NAME_BOOK_LAVKRAFT)

    @allure.step('Поиск цены книги')
    def find_price_book(self):
        return self.page.get_by_text(BookLocators.PRICE_BOOK)

    @allure.step('Поиск и клик по кнопке "Добавить в корзину"')
    def find_and_click_add_to_basket(self):
        return self.page.get_by_text(BookLocators.ADD_TO_BASKET).click()

    @allure.step('Поиск и клик по кнопке "Корзина"')
    def find_and_click_basket_btn(self):
        return self.page.get_by_role("link", name="Корзина").nth(1).click()    # не получается засунуть в локаторы

    @allure.step('Поиск текста "Оформить заказ"')
    def find_text_order(self):
        return self.page.get_by_text(BookLocators.CREATE_ORDER)

    @allure.step('Поиск и клик по кнопке "Оформить заказ"')
    def find_and_click_order_btn(self):
        return self.page.get_by_text(BookLocators.CREATE_ORDER).click()

    @allure.step('Поиск текста "Каталог" на странице сайта')
    def find_text_catalog(self):
        return self.page.get_by_role("heading", name="Каталог")

    @allure.step('Поиск и клик по кнопке "Авторы"')
    def find_btn_author(self):
        return self. page.get_by_role("button", name="Авторы").click()

    @allure.step('Поиск текста "Писатели"')
    def find_text_author(self):
        return self.page.get_by_role("heading", name="Писатели")

    @allure.step('Поиск списка авторов')
    def find_list_author(self):
        return self.get_by_text(BookLocators.AUTHOR_LIST)

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
        return self. page.get_by_role("heading", name="Условия работы для партнеров - селлеров")

    @allure.step('Поиск текста "Помощь"')
    def find_and_click_text_help(self):
        return self.page.get_by_text(BookLocators.HELP).click()

    @allure.step('Поиск текста "Помощь"')
    def find_text_help(self):
        return self.page.get_by_role("heading", name="Помощь")

    @allure.step('Поиск текста "Цены"')     #пока не знаю как проверить
    def find_and_click_text_price(self):
        return self.page.get_by_role("link", name="Цены").click()

    @allure.step('Поиск текста "FAQs"')
    def find_and_click_text_faq(self):
        return self.page.get_by_text(BookLocators.FAQ).click()

    @allure.step('Поиск текста "Каковы условия доставки и возврата товаров?"')
    def find_text_faq(self):
        return self.page.get_by_text("Каковы условия доставки и возврата товаров?")
