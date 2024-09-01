import pytest

from locators_book_room.page_locators import PageLocatorsBookRoom
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
