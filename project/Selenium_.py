from selenium import webdriver
from urllib.request import urlopen
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
import os

def get_directory(name) :
  
  try:
    if not os.path.exists(name + "/"):
      os.makedirs(name+ "/")
    directory = name + "/"
  except OSError:
    print('Error: Creating directory. '+ name + "/")
  
  return directory
        

def get_google_image(query, max_count) :
  driver = webdriver.Chrome() # 크롬드라이버 설치한 경로 작성 필요 
  driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl") # 구글 이미지 검색 url
  elem = driver.find_element(By.NAME,"q") #구글 검색창 선택
  elem.send_keys(query) # 검색창에 검색할 내용(name)넣기
  elem.send_keys(Keys.RETURN)
  
  SCROLL_PAUSE_TIME = 1
  directory = get_directory(query)

  last_height = driver.execute_script("return document.body.scrollHeight")

  while True:
      driver.execute_script("window.scrollTo(0, document. body.scrollHeight);")
      time.sleep(SCROLL_PAUSE_TIME)
      new_height = driver.execute_script("return document.body.scrollHeight")

      if new_height == last_height:
          try:
             driver.find_element(By.CSS_SELECTOR,".mye4qd").click()
          except:
              break
      last_height = new_height
      
  images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
  count = 1

  for image in images:
    try:
        image.click()
        time.sleep(2)
        imgUrl = image.get_attribute('src')
        urllib.request.urlretrieve(imgUrl, directory + query + "_" + str(count) + ".jpg")
        print("Image saved:" + query + "_" + str(count) + ".jpg")
        count += 1
        if count > max_count:
            break
    except:
        pass

  driver.close()

def get_naver_image(query, max_count) :
  driver = webdriver.Chrome() # 크롬드라이버 설치한 경로 작성 필요 
  url = "https://search.naver.com/search.naver?where=image&section=image&query="+query
  driver.get(url)
  
  SCROLL_PAUSE_TIME = 1
  directory = get_directory(query)

  last_height = driver.execute_script("return document.body.scrollHeight")

  while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
      
  images = driver.find_elements(By.CLASS_NAME, "_image")
  count = 1

  for image in images:
    try:
        image.click()
        time.sleep(2)
        imgUrl = image.get_attribute('src')
        urllib.request.urlretrieve(imgUrl, directory + query + "_" + str(count) + ".jpg")
        print("Image saved:" + query + "_" + str(count) + ".jpg")
        count += 1
        if count > max_count:
            break
    except:
        pass

  driver.close()

