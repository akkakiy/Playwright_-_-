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

    @allure.title('Поиск книги в каталоге по имени и фамилии автора')
    def test_search_author_full_name(self, browser_context, catalog_page):
        catalog_page.find_and_click_catalog()
        catalog_page.find_and_fill_placeholder_name_and_lastname_author()
        catalog_page.find_and_click_search_btn()
        book = catalog_page.find_name_book()
        price = catalog_page.find_price_book()
        expect(book).to_be_visible() and expect(price).to_be_visible()

    @allure.title('Поиск книги в каталоге по имени автора')
    def test_search_author_name(self, browser_context, catalog_page):
        catalog_page.find_and_click_catalog()
        catalog_page.find_and_fill_placeholder_name_author()
        catalog_page.find_and_click_search_btn()
        book = catalog_page.find_name_book()
        price = catalog_page.find_price_book()
        expect(book).to_be_visible() and expect(price).to_be_visible()

    @allure.title('Поиск книги в каталоге по фамилии автора')
    def test_search_author_lastname(self, browser_context, catalog_page):
        catalog_page.find_and_click_catalog()
        catalog_page.find_and_fill_placeholder_lastname_author()
        catalog_page.find_and_click_search_btn()
        book = catalog_page.find_name_book()
        price = catalog_page.find_price_book()
        expect(book).to_be_visible() and expect(price).to_be_visible()

    @allure.title('Добавление книги в корзину')
    def test_add_book_to_basket(self, catalog_page, browser_context):
        catalog_page.find_and_click_catalog()
        catalog_page.find_and_fill_placeholder_name_and_lastname_author()
        catalog_page.find_and_click_search_btn()
        catalog_page.find_name_book().click()
        catalog_page.find_and_click_add_to_basket()
        catalog_page.find_and_click_basket_btn()
        order = catalog_page.find_text_order()
        book = catalog_page.find_name_book()
        expect(order).to_be_visible() and expect(book).to_be_visible()
