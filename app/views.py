from django.shortcuts import render
from django.views.generic import View
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class IndexView(View):
    def get(self, request, *args, **kwargs):
        # Seleniumをあらゆる環境で起動させるChromeオプション
        options = Options()
        options.add_argument('--disable-gpu');
        options.add_argument('--disable-extensions');
        options.add_argument('--proxy-server="direct://"');
        options.add_argument('--proxy-bypass-list=*');
        options.add_argument('--start-maximized');
        options.add_argument('--headless'); # ヘッドレスモード

        DRIVER_PATH = './app/driver/chromedriver.exe' 

        # ブラウザの起動
        driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

        # Webページにアクセスする
        url = '{{ https://www.yahoo.co.jp }}'
        driver.get(url)

        return driver
        # return render(request, 'app/index.html')