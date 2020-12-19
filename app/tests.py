from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome.webdriver import WebDriver


class LoginTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(executable_path='./app/driver/chromedriver.exe')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        # ログインページを開く
        self.selenium.get('https://paiza.jp/sign_in' + str(reverse_lazy('login')))

        # ログイン
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('username')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('password')
        self.selenium.find_element_by_class_name('btn').click()

        # ページタイトルの検証
        self.assertEquals('ログイン後ページ', self.selenium.title)

# import time                            # スリープを使うために必要
# from selenium import webdriver         # Webブラウザを自動操作する（python -m pip install selenium)
# import chromedriver_binary             # パスを通すためのコード

# driver = webdriver.Chrome()            # Chromeを準備
# driver.get('https://www.google.com/')  # Googleを開く
# time.sleep(5)                          # 5秒間待機
# driver.quit() 