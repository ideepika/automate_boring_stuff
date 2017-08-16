from selenium import webdriver
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
#import time


# Create a new instance of the Firefox driver
driver = webdriver.Chrome('/home/deepika/chromedriver')


# go to the jec results
driver.get("http://www.jecjabalpur.ac.in/Exam/Programselect.aspx")
#sbox = driver.find_element_by_class_name("txtSearch")
#sbox.send_keys("Roll No.")
