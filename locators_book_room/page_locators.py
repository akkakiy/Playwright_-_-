import allure

from locators_book_room.base_page import BasePage


class PageLocatorsBookRoom(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @allure.step('Поиск и клик по кнопке "Каталог"')
    def find_and_click_catalog(self):
        return self.page.get_by_text('Каталог').click()

    @allure.step('Поиск и заполнение поля "Поиск по каталогу"')
    def find_and_fill_placeholder(self):
        return self.page.get_by_placeholder('Поиск по каталогу').fill('Ловец снов')

    @allure.step('Поиск и заполнение поля "Поиск по каталогу" по имени и фамилии автора')
    def find_and_fill_placeholder_name_and_lastname_author(self):
        return self.page.get_by_placeholder('Поиск по каталогу').fill('Говард Лавкрафт')

    @allure.step('Поиск и заполнение поля "Поиск по каталогу" по имени автора')
    def find_and_fill_placeholder_name_author(self):
        return self.page.get_by_placeholder('Поиск по каталогу').fill('Говард')

    @allure.step('Поиск и заполнение поля "Поиск по каталогу" по фамилии автора')
    def find_and_fill_placeholder_lastname_author(self):
        return self.page.get_by_placeholder('Поиск по каталогу').fill('Лавкрафт')

    @allure.step('Поиск и клик по кнопке "Поиск"')
    def find_and_click_search_btn(self):
        return self.page.locator('.search-btn').click()

    @allure.step('Поиск и клик по книге "Ловец снов"')
    def find_and_click_book(self):
        return self.page.get_by_text('Ловец снов').click()

    @allure.step('Поиск картинки "Ловец снов"')
    def find_img_book(self):
        return self.page.get_by_alt_text('img')

    @allure.step('Поиск по названия книги')
    def find_name_book(self):
        return self.page.get_by_text('Дагон')

    @allure.step('Поиск цены книги')
    def find_price_book(self):
        return self.page.get_by_text('870 руб.')

    @allure.step('Поиск и клик по кнопке "Добавить в корзину"')
    def find_and_click_add_to_basket(self):
        return self.page.get_by_text('Добавить в корзину').click()

    @allure.step('Поиск и клик по кнопке "Корзина"')
    def find_and_click_basket_btn(self):
        return self.page.get_by_role("link", name="Корзина").nth(1).click()

    @allure.step('Поиск текста "Оформить заказ"')
    def find_text_order(self):
        return self.page.get_by_text('Оформить заказ')

    @allure.step('Поиск и клик по кнопке "Оформить заказ"')
    def find_and_click_order_btn(self):
        return self.page.get_by_text('Оформить заказ').click()
