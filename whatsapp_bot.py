# necessary import from selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# start the chrome driver 
driver = webdriver.Chrome()
# get the browser to open whatsapp url
driver.get("https://web.whatsapp.com/")

# tell the program to sleep for 1 min while you scan barcode and wait for network
time.sleep(60)

#  identify the contact you want to send to
names = ["Chinelo"]

for name in names:
#  statement where to find the contact with the xpath 
    person = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    person.click()
#loop for the screen
    for i in range(1,3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    msg_got = driver.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
    msg = [message.text for message in msg_got]

    if msg[-1] == "Happy New Month":
        reply = driver.find_element_by_xpath('//div[@class="_1Plpp"]')
        
        reply.send_keys("Same to you")
        reply = driver.find_element_by_xpath('//button[@class="_35EW6"]')
        reply.click()
    else :
        reply = driver.find_element_by_xpath('//div[@class="_1Plpp"]')
        
        reply.send_keys("Happy New Month")
        reply = driver.find_element_by_xpath('//button[@class="_35EW6"]')
        reply.click()
