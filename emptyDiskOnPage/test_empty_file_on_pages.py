# -*- coding: utf-8 -*-
import json

import allure
import pytest
from .pages.locators import ThematicPageLocators
from .pages.base_page import BasePage
pages = []


@pytest.mark.parametrize("tpage", pages)
def test_empty_files_on_pages(browser, tpage):
    link = tpage
    page = BasePage(browser, link)
    page.open()
    files = browser.find_elements(*ThematicPageLocators.ALL_FILES_TO_CHEK)
    print(f"Количество файлов {len(files)}")
    empty_files = 0
    for file in files:
        file_name = json.loads(file.get_attribute("data-actions"))[2]['params']['name']
        print(file_name)
        if file_name is None:
            empty_files += 1
    assert empty_files == 0, f"Тематическая страница по ссылке:\n{link}\nимеет пустые файлы!\nВсего обнаружено {empty_files} пустых файлов."





