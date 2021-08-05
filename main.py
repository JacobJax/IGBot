from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
import random

driver = webdriver.Firefox()


class Bot:

    def __init__(self, user, pwd):
        self.username = user
        self.password = pwd

    def log_in(self, user_inp, pwd_inp):
        user_inp.send_keys(self.username)
        pwd_inp.send_keys(self.password)
        pwd_inp.send_keys(Keys.ENTER)


    def like_pics(self, like_elm, next_elm, close_elm, num_of_pics):
        while True:

            driver.implicitly_wait(30)

            for i in range(num_of_pics):
                driver.implicitly_wait(10)
                like_elm.click()
                print('Liked ❤')

                driver.implicitly_wait(10)
                next_elm.click()

            close_elm.click()
            time.sleep(random.randint(3, 7))
            driver.refresh()

            # if datetime.now == 10:
            #     break


# ask for username and password
username = input('Enter Username: ')
password = input('Enter password: ')

term = input('Enter hashtag to search: ')
print('\n')

driver.get('https://www.instagram.com/')

# instanciate Bot class
bot = Bot(username, password)

driver.implicitly_wait(5)

# username input
uname_path = 'div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)'
uname = driver.find_element(By.CSS_SELECTOR, uname_path)

# password input
pwd_path = 'div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)'
pwd = driver.find_element(By.CSS_SELECTOR, pwd_path)

# log in to instagram
bot.log_in(uname, pwd)

# close modals
driver.implicitly_wait(30)

not_now = driver.find_element(By.CSS_SELECTOR, 'button.sqdOP:nth-child(4)')
driver.implicitly_wait(5)
not_now.click()

driver.implicitly_wait(30)

driver.find_element(By.CSS_SELECTOR, 'button.aOOlW:nth-child(2)').click()


# search for hashtag
search = driver.find_element(By.CSS_SELECTOR, '.eyXLr')
driver.implicitly_wait(10)
search.click()

driver.implicitly_wait(10)
search = driver.find_element(By.CSS_SELECTOR, '.XTCLo')

search.send_keys(term)
search.send_keys(Keys.ENTER)
driver.find_elements_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div')[0].click()

driver.implicitly_wait(10)
driver.find_elements_by_xpath('/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]')[0].click()
# /html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]

like_elm = driver.find_element(By.CSS_SELECTOR, '.fr66n > button:nth-child(1)')
# .fr66n > button:nth-child(1)
# /html/body/div[6]/div[2]/div/article/div[3]/section[1]/span[1]/button

next_elm = driver.find_element(By.CSS_SELECTOR, '._65Bje')
# ._65Bje

close_elm = driver.find_element(By.CSS_SELECTOR, '.BI4qX > button:nth-child(1)')
# .BI4qX > button:nth-child(1)

driver.implicitly_wait(30)
# bot.like_pics(like_elm, next_elm, close_elm, 4)

while True:
    for i in range(4):
        driver.implicitly_wait(10)
        like_elm.click()
        print('Liked ❤')
        
        driver.implicitly_wait(10)
        next_elm.click()
        
        like_elm = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/article/div[3]/section[1]/span[1]/button')

    driver.implicitly_wait(10)
    close_elm.click()

    driver.refresh()
    time.sleep(random.randint(4, 10))
    driver.find_elements_by_xpath('/html/body/div[1]/section/main/article/div[1]/div/div/div[3]')[0].click()
    like_elm = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/article/div[3]/section[1]/span[1]/button')
    next_elm = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div/a[2]')
    close_elm = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/button')
        



