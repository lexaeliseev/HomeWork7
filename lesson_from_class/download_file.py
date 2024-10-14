import time

from selene import browser
from selenium import webdriver

from conftest import TMP_DIR

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": TMP_DIR,

    "download.prompt_for_download": False
}
options.add_experimental_option("prefs", prefs)
browser.config.driver_options = options


browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")
browser.element("[data-testid='download-raw-button']").click()
time.sleep(3)
