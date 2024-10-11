import sys
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTime, pyqtSignal, QObject, QThread, QMutex, QWaitCondition
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from my_form import Ui_Dialog
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re

class ScraperThread(QThread):
    data_scraped = pyqtSignal(pd.DataFrame)

    def __init__(self):
        super().__init__()
        self.is_running = True
        self.is_paused = False
        self.mutex = QMutex()
        self.condition = QWaitCondition()

    def run(self):
        try:
            service = Service(executable_path=r'D:\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
            driver = webdriver.Chrome(service=service)

            phone_names = []
            phone_conditions = []
            phone_prices = []
            shipping_costs = []
            locations = []
            sellers_info = []
            quantities_sold = []

            driver.get('https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&Brand=Huawei%7CNokia%7COPPO%7CGoogle%7CRedmi%7CVIVO&_nkw=mobile+phones&_ipg=240&rt=nc&_pgn=1')

            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "s-item__info"))
            )

            def extract_data():
                content = driver.page_source
                soup = BeautifulSoup(content, 'html.parser')
                items = soup.findAll('div', attrs={'class': 's-item__info clearfix'})

                for item in items:
                    name_element = item.find('div', attrs={'class': 's-item__title'})
                    phone_name = name_element.text.strip() if name_element else 'Name not found'
                    condition_element = item.find('span', attrs={'class': 'SECONDARY_INFO'})
                    phone_condition = condition_element.text.strip() if condition_element else 'Condition not found'
                    price_element = item.find('span', attrs={'class': 's-item__price'})
                    phone_price = price_element.text.strip() if price_element else 'Price not found'
                    shipping_element = item.find('span', attrs={'class': 's-item__shipping s-item__logisticsCost'})
                    shipping_cost = shipping_element.text.strip() if shipping_element else 'Shipping cost not found'
                    location_element = item.find('span', attrs={'class': 's-item__location s-item__itemLocation'})
                    location = location_element.text.strip() if location_element else 'Location not found'
                    seller_element = item.find('span', attrs={'class': 's-item__seller-info-text'})
                    seller_info = seller_element.text.strip() if seller_element else 'Seller info not found'
                    quantity_sold = item.find('span', attrs={'class': 's-item__dynamic s-item__quantitySold'})
                    quantity = quantity_sold.text.strip() if quantity_sold else 'Quantity sold not found'

                    phone_names.append(phone_name)
                    phone_conditions.append(phone_condition)
                    phone_prices.append(phone_price)
                    shipping_costs.append(shipping_cost)
                    locations.append(location)
                    sellers_info.append(seller_info)
                    quantities_sold.append(quantity)

            page_count = 30
            for _ in range(page_count):
                if not self.is_running:
                    break

                self.mutex.lock()
                while self.is_paused:
                    self.condition.wait(self.mutex)
                self.mutex.unlock()

                extract_data()  # Extract data from the current page

                try:
                    next_button = driver.find_element(By.CSS_SELECTOR, "a.pagination__next.icon-link")
                    next_button.click()
                    time.sleep(3)
                except Exception as e:
                    print(f"Error occurred while navigating to the next page: {e}")
                    break

            df = pd.DataFrame({
                'Phone Name': phone_names,
                'Condition': phone_conditions,
                'Price': phone_prices,
                'Shipping Cost': shipping_costs,
                'Location': locations,
                'Seller Info': sellers_info,
                'Quantity Sold': quantities_sold
            })

            self.data_scraped.emit(df)  # Emit the scraped data

        except Exception as e:
            print(f"Error occurred in scraper thread: {e}")
        finally:
            driver.quit()

    def stop(self):
        self.is_running = False

    def pause(self):
        self.is_paused = True

    def resume(self):
        self.is_paused = False
        self.condition.wakeAll()
    