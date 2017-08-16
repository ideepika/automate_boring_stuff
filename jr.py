from selenium import webdriver
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
#import time


# Create a new instance of the Firefox driver
driver = webdriver.Chrome('/home/deepika/chromedriver')


#to go to jec result page
driver.get("http://www.jecjabalpur.ac.in/Exam/Programselect.aspx")
sbox = driver.find_element_by_xpath("//input[@id='radlstProgram_0']").click()
#sbox.send_keys("Roll No.")
#to select the roll no field
python_button = driver.find_element_by_xpath("//input[@id='txtrollno']").click()

#type text
text_area = driver.find_element_by_id('txtrollno')
text_area.send_keys('0201IT151020')

#click submit button
submit_button = driver.find_element_by_xpath("//input[@id='btnviewresult']").click()
# go to the jec results

