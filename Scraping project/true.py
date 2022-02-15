from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from csv import writer
import time
import re

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


#USA total State list
state = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut",
      "Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky",
      "Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri",
      "Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina",
      "North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota",
      "Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

driver = webdriver.Chrome('/home/tanbir/Documents/chromedriver_linux64/chromedriver')

#link
driver.get('https://storelocator.truevalue.com/index2015.new.html?preferredStore=4F1QJ578-C0GT-A0X9-Y2SD-3MWOIY647P6A')

time.sleep(2)


search_bar = driver.find_element_by_xpath('//*[@id="inputaddress"]')

time.sleep(3)

for x in state:

    search_bar.send_keys(x)

    search_bar.send_keys(Keys.RETURN)

    ele = driver.find_element_by_xpath('//*[@id="submit-button"]')

    ele.click()

    time.sleep(5)

    search = driver.find_element_by_xpath('//div[@class="poi"]/h3')
    #FIND NUMBER TEXT TOTAL STORE BUT THIS DATA IS HIDDEN STYLE
    

    p=search.get_attribute('textContent')
    #HIDDEN STYLE TEXT SHOW

    k=re.findall('\d+', p )
    #FIND INTEGER IN LIST CUT OFF STRING

    res = list(map(int, k))
    #CONVERT LIST TO INTEGER

    n=res[0]
    #INDEX PRINT
    
    print(type(n))
    #CHECK TYPE


    info={}

    for i in range(1,n+1):
        pname = '(//*[@class="viewBubble"])['+str(i)+']'
        paddress = '(//*[@class="address_row"]//*[@style="width:auto;"])['+str(i)+']'
        pphone = '(*//span[@class="addressdiv desktopphone"]/span)['+str(i)+']'

        try:
            name = driver.find_element_by_xpath(pname).text #for all list data acess
        except:
            name = " "
        
        try:
            address =driver.find_element_by_xpath(paddress).text
        except:
            address = " "

        try:
            phone = driver.find_element_by_xpath(pphone).text
        except:
            phpne = " "

        info.update({
            "State": x,
            "Name" : name,
            "Address": address,
            "Phone" : phone
        })
        print(info)
        listOfValues = info.values() 
        listOfValues = list(listOfValues)
        try:
            append_list_as_row('true.csv',listOfValues)

        except:
            print("I/O error")

    search_bar.clear()
    time.sleep(2)

 

driver.close()