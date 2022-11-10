import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
FAVORITE_ACCOUNT = os.environ.get("FAVORITE_ACCOUNT")


class InstaFollower:
    def __init__(self):
        service = Service(executable_path=CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.instagram.com/accounts/login/")

    def login(self):
        user = self.driver.find_element(By.NAME, "username")
        user.send_keys(USERNAME)

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{FAVORITE_ACCOUNT}")

        sleep(2)
        followers = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        sleep(2)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')
        for i in range(20):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()
