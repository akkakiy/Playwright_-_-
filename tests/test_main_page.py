import allure

from playwright.sync_api import expect


@allure.suite('Каталог')
class TestSearchCatalog:

    @allure.title('Поиск книги в каталоге по названию')
    def test_search_book(self, browser_context, catalog_page):
        catalog_page.find_and_click_catalog()
        catalog_page.find_and_fill_placeholder()
        catalog_page.find_and_click_search_btn()
        catalog_page.find_and_click_book()
        book = catalog_page.find_img_book()
        expect(book).to_be_visible()
