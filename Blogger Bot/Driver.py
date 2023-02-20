from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime as dt
import pandas as pd
import time


class Reddit_Scraper:
    def __init__(self, url, u_id, password, sub, driver_loc):
        self.Url = url
        self.U_id = u_id
        self.Password = password
        self.Sub = sub
        self.Driver_loc = driver_loc

    def login(self):
        global driver
        driver = webdriver.Chrome(self.Driver_loc)
        driver.get(self.Url)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/header/div/div[2]/div/div[1]/a").click()
        id_loc = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[1]/div/div/form/fieldset[1]/input")))
        pass_loc = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div/div/form/fieldset[2]/input")
        id_loc.send_keys(self.u_id)
        pass_loc.send_keys(self.password)
        driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button").click()
        search_bar = driver.find_element(By.XPATH,
                                         "/html/body/div[1]/div/div[2]/div[1]/header/div/div[1]/div[3]/div/form/input")
        search_bar.send_keys(self.sub)
        search_bar.send_keys(Keys.ENTER)
        search_bar.send_keys(Keys.ENTER)

    def scrape(self, n_prompts):

        prompts = []
        for i in range(3, n_prompts):
            try:
                element = driver.find_element(By.XPATH,
                                              "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[4]/div["
                                              "1]/div[ "
                                              "5]/div[{}]".format(
                                                  i))
                string = element.text
                if "Promoted" in string:
                    continue
                prompts.append(string.strip())
            except:
                pass
