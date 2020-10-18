#Selenium imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import os
import wget
from posix import getcwd

driver = webdriver.Chrome ('/Users/retina/Documents/PythonProjects/chromedriver')
driver.get('https://www.instagram.com/explore/tags/tarajidawla/')

se_connecter = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button [contains(text(), 'Se connecter')]" ))).click()

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))


username.clear()
password.clear()

username.send_keys('m03ez1919')
password.send_keys('password')


log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type ='submit']"))).click()

Plus_tard = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button [contains(text(), 'Plus tard')]" ))).click()
Plus_tard2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button [contains(text(), 'Plus tard')]" ))).click()


driver.execute_script("window.scrollTo(0,4000);")
images = driver.find_element_by_tag_name('img')
images = [image.get_attribute('src') for image in images ]

images
keyword = "tarajiDawla"

path = "/Users/retina/Documents/PythonProjects/images"
#path = os.path.join(path, keyword[1:] + "s" )
#os.mkdir(path)

counter = 0
for image in images :
    save_as = os.path.join(path,keyword[1:] + str (counter) + '.jpg')
    wget.download(image, save_as)
    counter =+ 1
