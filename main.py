import time
import os
import urllib
import requests
import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


def main():
    # авторизация
    with open('logs.txt', 'r') as f:
        logs = f.read().splitlines()
    driver = webdriver.Chrome()
    driver.get('https://smartreading.ru/user-unauthorized-message')
    driver.find_element_by_xpath(
        "//*[@class='auth--btnBox no_margin-top']").click()
    # time.sleep(5)
    driver.find_element_by_xpath(
        "//*[@class='vk-auth authAlter--item vkontakte vkontakte-1']").click()
    # time.sleep(5)
    log = driver.find_element_by_xpath(
        "//input[@type='text']")
    log.send_keys(logs[0])
    pas = driver.find_element_by_xpath(
        "//input[@type='password']")
    pas.send_keys(logs[1])
    driver.find_element_by_id('install_allow').click()

# парсинг
    # считывание
    """ count = 57
    part = 8
    ts = 5
    for i in range(63, 65):  # 65
        if (i == 63):
            for j in range(3, 10):
                driver.get(
                    f'https://smartreading.ru/summary?page={i}')
                driver.find_element_by_id(f'summaryNumber_{j}').click()
                time.sleep(0.7)
                name = driver.find_element_by_tag_name('h1').text

                nextpage = driver.find_element_by_xpath(
                    "//a[@class='productPlayer--tabItem']").get_attribute('href')
                driver.get(nextpage)
                name = name[:63].strip()
                while (name.find('?') != -1 or name.find('\\') != -1 or name.find('/') != -1 or name.find(':') != -1 or name.find('*') != -1 or name.find('"') != -1 or name.find('<') != -1 or name.find('>') != -1 or name.find('|') != -1):
                    if (name.find('?') != -1):
                        name = name.replace('?', '')
                    elif (name.find('\\') != -1):
                        name = name.replace('\\', '')
                    elif (name.find('/') != -1):
                        name = name.replace('/', '')
                    elif (name.find(':') != -1):
                        name = name.replace(':', '')
                    elif (name.find('"') != -1):
                        name = name.replace('"', '')
                    elif (name.find('<') != -1):
                        name = name.replace('<', '')
                    elif (name.find('>') != -1):
                        name = name.replace('>', '')
                    elif (name.find('|') != -1):
                        name = name.replace('|', '')

                path = f'C:\\Users\\Lord\\Desktop\\TrueBooks\\_{part}\\{count}.html'
                pg.hotkey('ctrl', 's')
                time.sleep(1)
                pg.typewrite(path)
                pg.hotkey('enter')
                time.sleep(ts)

                os.mkdir(
                    f"C:\\Users\\Lord\\Desktop\\TrueBooks\\_{part}\\{name}")
                os.rename(f'C:\\Users\\Lord\\Desktop\\TrueBooks\\_{part}\\{count}.html',
                          f'C:\\Users\\Lord\\Desktop\\TrueBooks\\_{part}\\{name}.html')
                os.replace(
                    f'C:\\Users\\Lord\\Desktop\\TrueBooks\\_{part}\\{count}_files', f'C:\\Users\\Lord\\Desktop\\TrueBooks\\_{part}\\{name}\\{count}_files')
                os.replace(f'C:\\Users\\Lord\\Desktop\\TrueBooks\\_{part}\\{name}.html',
                           f'C:\\Users\\Lord\\Desktop\\TrueBooks\\_{part}\\{name}\\{name}.html')

                # html = driver.page_source
                # f = open(f'books/{name}.html', 'w', encoding='utf-8')
                # f.write(html)
                print(f'{count} {i} {j} {name}')
                count += 1
        else:
            for j in range(1, 10):
                driver.get(
                    f'https://smartreading.ru/summary?page={i}')
                driver.find_element_by_id(f'summaryNumber_{j}').click()
                time.sleep(0.7)
                name = driver.find_element_by_tag_name('h1').text

                nextpage = driver.find_element_by_xpath(
                    "//a[@class='productPlayer--tabItem']").get_attribute('href')
                driver.get(nextpage)
                name = name[:63].strip()
                while (name.find('?') != -1 or name.find('\\') != -1 or name.find('/') != -1 or name.find(':') != -1 or name.find('*') != -1 or name.find('"') != -1 or name.find('<') != -1 or name.find('>') != -1 or name.find('|') != -1):
                    if (name.find('?') != -1):
                        name = name.replace('?', '')
                    elif (name.find('\\') != -1):
                        name = name.replace('\\', '')
                    elif (name.find('/') != -1):
                        name = name.replace('/', '')
                    elif (name.find(':') != -1):
                        name = name.replace(':', '')
                    elif (name.find('"') != -1):
                        name = name.replace('"', '')
                    elif (name.find('<') != -1):
                        name = name.replace('<', '')
                    elif (name.find('>') != -1):
                        name = name.replace('>', '')
                    elif (name.find('|') != -1):
                        name = name.replace('|', '')

                path = f'C:\\Users\\Lord\\Desktop\\TrueBooks\\_{part}\\{count}.html'
                pg.hotkey('ctrl', 's')
                time.sleep(1)
                pg.typewrite(path)
                pg.hotkey('enter')
                time.sleep(ts)

                os.mkdir(
                    f"C:\\Users\\Lord\\Desktop\\TrueBooks\\_{part}\\{name}")
                os.rename(f'C:\\Users\\Lord\\Desktop\\TrueBooks\\_{part}\\{count}.html',
                          f'C:\\Users\\Lord\\Desktop\\TrueBooks\\_{part}\\{name}.html')
                os.replace(
                    f'C:\\Users\\Lord\\Desktop\\TrueBooks\\_{part}\\{count}_files', f'C:\\Users\\Lord\\Desktop\\TrueBooks\\_{part}\\{name}\\{count}_files')
                os.replace(f'C:\\Users\\Lord\\Desktop\\TrueBooks\\_{part}\\{name}.html',
                           f'C:\\Users\\Lord\\Desktop\\TrueBooks\\_{part}\\{name}\\{name}.html')

                # html = driver.page_source
                # f = open(f'books/{name}.html', 'w', encoding='utf-8')
                # f.write(html)
                print(f'{count} {i} {j} {name}')
                count += 1 """

# сбор по категориям

# считывание
    count = 0
    selfDevelopment = []
    zoj = []
    family = []
    society = []
    bussines = []
    money = []
    technology = []
    for i in range(1, 65):  # 65
        driver.get(
            f'https://smartreading.ru/summary?page={i}')
        time.sleep(0.2)

        titles = driver.find_elements_by_xpath(
            "//div[@class='productItem--title']")
        janres = driver.find_elements_by_xpath(
            "//a[@class='productItem--infoType']")
        for j in range(len(titles)):
            name = titles[j].text
            name = name[:63].strip()
            while (name.find('?') != -1 or name.find('\\') != -1 or name.find('/') != -1 or name.find(':') != -1 or name.find('*') != -1 or name.find('"') != -1 or name.find('<') != -1 or name.find('>') != -1 or name.find('|') != -1):
                if (name.find('?') != -1):
                    name = name.replace('?', '')
                elif (name.find('\\') != -1):
                    name = name.replace('\\', '')
                elif (name.find('/') != -1):
                    name = name.replace('/', '')
                elif (name.find(':') != -1):
                    name = name.replace(':', '')
                elif (name.find('"') != -1):
                    name = name.replace('"', '')
                elif (name.find('<') != -1):
                    name = name.replace('<', '')
                elif (name.find('>') != -1):
                    name = name.replace('>', '')
                elif (name.find('|') != -1):
                    name = name.replace('|', '')

            if (janres[j].text.lower() == 'саморазвитие'):
                selfDevelopment.append(name)
            if (janres[j].text.lower() == 'бизнес'):
                bussines.append(name)
            if (janres[j].text.lower() == 'деньги'):
                money.append(name)
            if (janres[j].text.lower() == 'технологии'):
                technology.append(name)
            if (janres[j].text.lower() == 'общество'):
                society.append(name)
            if (janres[j].text.lower() == 'семья'):
                family.append(name)
            if (janres[j].text.lower() == 'зож'):
                zoj.append(name)

        count += 1
        print(count)

    with open(f"new/selfDevelopment.txt", "w") as file:
        for item in selfDevelopment:
            file.write("%s\n" % item)
    with open(f"new/bussines.txt", "w") as file:
        for item in bussines:
            file.write("%s\n" % item)
    with open(f"new/money.txt", "w") as file:
        for item in money:
            file.write("%s\n" % item)
    with open(f"new/technology.txt", "w") as file:
        for item in technology:
            file.write("%s\n" % item)
    with open(f"new/society.txt", "w") as file:
        for item in society:
            file.write("%s\n" % item)
    with open(f"new/family.txt", "w") as file:
        for item in family:
            file.write("%s\n" % item)
    with open(f"new/zoj.txt", "w") as file:
        for item in zoj:
            file.write("%s\n" % item)


if __name__ == '__main__':
    main()
