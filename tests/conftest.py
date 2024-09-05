import pytest

from pages.page_footer import PageFooter
from pages.page_main_catalog import PageLocatorsBookRoom
from url import Urls


@pytest.fixture
def browser_context(page):
    page.goto(Urls.MAIN_PAGE)
    return {
        'viewport': {'width': 1920, 'height': 1080},
    }


@pytest.fixture
def catalog_page(page):
    return PageLocatorsBookRoom(page)


@pytest.fixture
def main_page(page):
    return PageLocatorsBookRoom(page)


@pytest.fixture
def page_footer(page):
    return PageFooter(page)
