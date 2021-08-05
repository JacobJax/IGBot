from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
import random


uname = input('Enter Instagram Username: ')
pwd = input('Enter Instagram Password: ')
search_term = input('Enter Hashtag: ')

print('\n Processing.......')

driver = webdriver.Firefox()
driver.get('https://www.instagram.com/')


# Element selectors
username_selector = 'div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)'
password_selector = 'div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)'

# not now button 1 and 2
not_now_selector = 'button.sqdOP:nth-child(4)'
not_now2_selector = 'button.aOOlW:nth-child(2)'

# search input
search_selector = '.eyXLr'
search_selector2 = '.XTCLo'

# results from search
results_xpath = '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div'

# navigate to recent posts div
recent_div_xpath = '/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]'
recent_div_xpath2 = '/html/body/div[1]/section/main/article/div[1]/div/div/div[3]'

# like button
like_selector = '.fr66n > button:nth-child(1)'
like_xpath = '/html/body/div[6]/div[2]/div/article/div[3]/section[1]/span[1]/button'
like_xpath2 = '/html/body/div[6]/div[2]/div/article/div[3]/section[1]/span[1]/button'

# next button
next_selector = '._65Bje'
next_xpath = '/html/body/div[6]/div[1]/div/div/a[2]'

# close button
close_selector = '.BI4qX > button:nth-child(1)'
close_xpath = '/html/body/div[6]/div[3]/button'



##################################################
# functionality
##################################################


# log in to instagram
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, username_selector).send_keys(uname)
driver.find_element(By.CSS_SELECTOR, password_selector).send_keys(pwd)

driver.find_element(By.CSS_SELECTOR, password_selector).send_keys(Keys.ENTER)


# close instagram modal popups
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, not_now_selector).click()
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, not_now2_selector).click()


# search for hashtag
driver.implicitly_wait(10)
search = driver.find_element(By.CSS_SELECTOR, search_selector).click()
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, search_selector2).send_keys(search_term)
driver.find_element(By.CSS_SELECTOR, search_selector2).send_keys(Keys.ENTER)


# select search result
driver.find_elements_by_xpath(results_xpath)[0].click()

# click on recent posts
driver.implicitly_wait(20)
driver.find_elements_by_xpath(recent_div_xpath)[0].click()


# like pictures
like_btn = driver.find_element(By.CSS_SELECTOR, like_selector)
next_btn = driver.find_element(By.CSS_SELECTOR, next_selector)
close_btn = driver.find_element(By.CSS_SELECTOR, close_selector)

while True:
    try:
        for i in range(4):
            driver.implicitly_wait(10)
            like_btn.click()
            print('Liked ❤')

            driver.implicitly_wait(10)
            next_btn.click()

            like_btn = driver.find_element(By.XPATH, like_xpath)

        driver.implicitly_wait(10)
        close_btn.click()

        driver.refresh()
        time.sleep(random.randint(3, 5))

        driver.find_elements_by_xpath(recent_div_xpath2)[0].click()

        like_btn = driver.find_element(By.XPATH, like_xpath2)
        next_btn = driver.find_element(By.XPATH, next_xpath)
        close_btn = driver.find_element(By.XPATH, close_xpath)

    except Exception as e:
        print(f'Umbwakni 👎\n{e}')
        driver.quit()
