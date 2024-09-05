import allure

from playwright.sync_api import expect


@allure.suite('Проверка главной страницы')
class TestMainPage:

    @allure.title('Проверка кнопки "Каталог" на главной странице')
    def test_search_btn(self, browser_context, main_page):
        main_page.find_and_click_catalog()
        catalog = main_page.find_text_catalog()
        placeholder = main_page.find_placeholder()
        expect(catalog).to_be_visible() and expect(placeholder).to_be_visible()

    @allure.title('Проверка кнопки "Авторы" на главной странице')
    def test_author_btn(self, browser_context, main_page):
        main_page.find_btn_author()
        author = main_page.find_text_author()
        authors_list = main_page.find_list_author()
        expect(author).to_be_visible() and expect(authors_list).to_be_visible()

    @allure.title('Проверка кнопки "Партнерам по доставке" в футере')
    def test_delivery_link(self, browser_context, page_footer):
        page_footer.find_and_click_text_delivery()
        delivery = page_footer.find_text_delivery()
        expect(delivery).to_be_visible()

    @allure.title('Проверка кнопки "Партнерам-селерам" в футере')
    def test_salers_link(self, browser_context, page_footer):
        page_footer.find_and_click_text_selers()
        salers = page_footer.find_text_selers()
        expect(salers).to_be_visible()

    @allure.title('Проверка кнопки "Помощь" в футере')
    def test_help_link(self, browser_context, page_footer):
        page_footer.find_and_click_text_help()
        help_link = page_footer.find_text_help()
        expect(help_link).to_be_visible()

    @allure.title('Проверка ссылки "FAQs" в футере')
    def test_faq_link(self, browser_context, page_footer):
        page_footer.find_and_click_text_faq()
        faq = page_footer.find_text_faq()
        expect(faq).to_be_visible()
