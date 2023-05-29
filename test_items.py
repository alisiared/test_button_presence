import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207//"

def test_button_presence(browser):
    browser.get(link)
    #time.sleep(30)
    assert browser.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")