from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date


def read_info(driver, xpath):
    info_list = []
    for n in range(1, 4):
        tablecell = driver.find_element_by_xpath(xpath + '/table/tbody/tr/td[{0}]'.format(n))
        info_list.append(str('{:,}'.format(int(tablecell.get_attribute('data-absolute-value'))).replace(',', ' ')))
        try:
            difference = driver.find_element_by_xpath(xpath + '/table/tbody/tr/td[{0}]/div[3]/div'.format(n))
            number = difference.text.replace('.', ' ')
            info_list.append("(" + number + ")")
        except NoSuchElementException:
            info_list.append("")
            continue
    return info_list


def get_website():
    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=chrome-data")
    driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
    driver.get('https://www.google.de/search?source=hp&ei=RqnHX-bMNInhUP61iOgM&q=aktuelle+corona+zahlen&oq=aktue&gs_lcp'
               '=CgZwc3ktYWIQAxgAMgUIABDJAzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADoCCC46CAguEMcBEKMCUPMQWPUWYO'
               'EcaAFwAHgAgAGIAYgBzAOSAQMzLjKYAQCgAQGqAQdnd3Mtd2l6sAEA&sclient=psy-ab')
    sleep(3)
    # driver.find_element_by_xpath('//*[@id="agreeButton"]').click()
    # driver.find_element_by_xpath('//input[@title="Search"]') \
    #    .send_keys('aktuelle Corona zahlen')
    # driver.find_element_by_xpath('//input[@title="Search"]') \
    #    .send_keys(Keys.ENTER)
    germany = '/html/body/div[7]/div[2]/div[10]/div[1]/div[3]/div[2]/div/div/div/div/div[2]/div[1]/div/div[2]'
    germany_info = read_info(driver, germany)
    worldwide = '/html/body/div[7]/div[2]/div[10]/div[1]/div[3]/div[2]/div/div/div/div/div[2]/div[1]/div/div[3]'
    worldwide_info = read_info(driver, worldwide)
    driver.close()
    return [germany_info, worldwide_info]


def get_message():
    info_list = get_website()
    print(info_list)
    today = date.today()
    today = today.strftime("%d.%m.%Y")
    message = "Aktuelle Corona-Zahlen:\n" \
              "Heute am {0} gibt es in Deutschland:\n\n" \
              "{1} Fälle insgesamt {2}\n" \
              "{3} Genesene {4}\n" \
              "{5} Todesfälle {6}\n\n" \
              "Weltweit gibt es somit:\n\n" \
              "{7} Fälle insgesamt {8}\n" \
              "{9} Genesene {10}\n" \
              "{11} Todesfälle {12}\n" \
        .format(today, info_list[0][0], info_list[0][1], info_list[0][2], info_list[0][3], info_list[0][4],
                info_list[0][5], info_list[1][0], info_list[1][1], info_list[1][2], info_list[1][3], info_list[1][4],
                info_list[1][5])
    return message
