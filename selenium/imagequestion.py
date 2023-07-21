# # from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.support.ui import Select
# # from selenium.webdriver.common.by import By
# # from PIL import Image
# # import pytesseract
# # import time

# # driver = webdriver.Chrome()

# # login_url = 'https://adl.edu.tw/login.php'
# # driver.get(login_url)

# # select_county= driver.find_element(By.NAME, 'school[0]')
# # county_select = Select(select_county)
# # select_district= driver.find_element(By.NAME, 'school[1]')
# # district_select = Select(select_district)
# # select_school= driver.find_element(By.NAME, 'school[2]')
# # school_select = Select(select_school)
# # username_input = driver.find_element(By.NAME, 'username')
# # password_input = driver.find_element(By.NAME, 'password')
# # county = '臺中市'
# # district = '西區'
# # school = '中展國小'
# # username = 't042701'
# # password = 'Aa123456'
# # county_select.select_by_value(county)
# # county_select.select_by_value(district)
# # county_select.select_by_value(school)
# # username_input.send_keys(username)
# # password_input.send_keys(password)


# # input('"Enter" to close the driver')
# # driver.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()

# login_url = 'https://adl.edu.tw/login.php'
# driver.get(login_url)

# # 等待縣市下拉選單出現，並選擇縣市
# county_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'school[0]')))
# county = '臺中市'
# county_select = Select(county_select)
# county_select.select_by_value(county)

# # 等待區域下拉選單出現，並選擇區域
# district_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'school[1]')))
# district = '403-西區'
# district_select = Select(district_select)
# district_select.select_by_value(district)

# # 等待學校下拉選單出現，並選擇學校
# school_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'school[2]')))
# school = '190042-中展國小'
# school_select = Select(school_select)
# school_select.select_by_value(school)

# # 繼續其他操作，例如填寫帳號和密碼，然後提交表單
# username_input = driver.find_element(By.NAME, 'username')
# password_input = driver.find_element(By.NAME, 'password')
# username = 't042701'
# password = 'Aa123456'
# username_input.send_keys(username)
# password_input.send_keys(password)

# # 提交登入表單
# # ...
# input('"Enter" to close the driver')
# driver.close()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from io import BytesIO
import pytesseract
import base64
import time
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 初始化Selenium瀏覽器

option = webdriver.ChromeOptions()

option.add_experimental_option('useAutomationExtension', False)
option.add_experimental_option('excludeSwitches', ['enable-automation'])

login_url = 'https://adl.edu.tw/HomePage/home/'
driver = webdriver.Chrome(options=option)
driver.get(login_url)

# 等待縣市下拉選單出現，並選擇縣市
# county_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'school[0]')))
# county = '臺中市'
# county_select = Select(county_select)
# county_select.select_by_value(county)

# # 等待區域下拉選單出現，並選擇區域
# district_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'school[1]')))
# district = '403-西區'
# district_select = Select(district_select)
# district_select.select_by_value(district)

# # 等待學校下拉選單出現，並選擇學校
# school_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'school[2]')))
# school = '190042-中展國小'
# school_select = Select(school_select)
# school_select.select_by_value(school)

# # 等待驗證碼圖片元素出現，並截取驗證碼圖片
# # 等待驗證碼圖片元素出現
# # image_path = r'.\securimage_show.php'
# # img = Image.open(image_path)

# # # 使用 Tesseract OCR 進行圖片識別
# # captcha_text = pytesseract.image_to_string(img, config='--psm 6')

# # print("識別結果：", captcha_text)

# # 繼續其他操作，例如填寫帳號和密碼，然後提交表單
# username_input = driver.find_element(By.NAME, 'username')
# password_input = driver.find_element(By.NAME, 'password')
# username = 't042701'
# password = 'Aa123456'
# username_input.send_keys(username)
# password_input.send_keys(password)

# # 提交登入表單
# # ...

input('"Enter" to close the driver')
driver.close()
# 'C:\Users\yexua\OneDrive\桌面\tesseract-ocr-w64-setup-5.3.1.20230401'