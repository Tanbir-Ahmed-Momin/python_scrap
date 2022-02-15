from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/home/tanbir/Documents/chromedriver_linux64/chromedriver')
driver.get('https://storelocator.truevalue.com/index2015.new.html?preferredStore=4F1QJ578-C0GT-A0X9-Y2SD-3MWOIY647P6A')
print(driver.title)
time.sleep(2)
search_bar = driver.find_element_by_xpath('//*[@id="inputaddress"]')
time.sleep(3)
#search_bar.clear()
search_bar.send_keys("idaho")
search_bar.send_keys(Keys.RETURN)
ele = driver.find_element_by_xpath('//*[@id="submit-button"]')
ele.click()
time.sleep(5)
info=[]

for oree in driver.find_element_by_xpath('//*[@class="poi-item default"]'):
  name = oree.find_element_by_xpath('//*[@class="viewBubble"]').text #for all list data acess
  address =oree.find_element_by_xpath('//*[@class="address_row"]//*[@style="width:auto;"]').text
  phone = oree.find_element_by_xpath('*//span[@class="addressdiv desktopphone"]/span').text

  info.append(
     {
         "Name" : name,
         "Address": address,
         "Phone" : phone
              }
  )       

print(info)

driver.close()