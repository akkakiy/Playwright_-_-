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

    @allure.step('Поиск и клик по кнопке "Поиск"')
    def find_and_click_search_btn(self):
        return self.page.locator('.search-btn').click()

    @allure.step('Поиск и клик по книге "Ловец снов"')
    def find_and_click_book(self):
        return self.page.get_by_text('Ловец снов').click()

    @allure.step('Поиск картинки "Ловец снов"')
    def find_img_book(self):
        return self.page.get_by_alt_text('img')
