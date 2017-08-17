from selenium import webdriver
import base64
from os import system


# Create a new instance of the Firefox driver
driver = webdriver.Chrome('/home/sandesh/projects/automate_boring_stuff/chromedriver')


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


dropdown = driver.find_element_by_id("drpSemester")
driver.find_element_by_xpath("//select[@id='drpSemester']/option[@value='4']").click()

#driver.switch_to.frame("Main")

# find the captcha element
ele_captcha = driver.find_element_by_xpath("//*[@id='pnlCaptcha']/table/tbody/tr[1]/td/div/img")

# get the captcha as a base64 string
img_captcha_base64 = driver.execute_async_script("""
    var ele = arguments[0], callback = arguments[1];
    ele.addEventListener('load', function fn(){
      ele.removeEventListener('load', fn, false);
      var cnv = document.createElement('canvas');
      cnv.width = this.width; cnv.height = this.height;
      cnv.getContext('2d').drawImage(this, 0, 0);
      callback(cnv.toDataURL('image/jpeg').substring(22));
    }, false);
    ele.dispatchEvent(new Event('load'));
    """, ele_captcha)

# save the captcha to a file
with open(r"captcha.jpg", 'wb') as f:
    f.write(base64.b64decode(img_captcha_base64))



system("tesseract -l eng /home/sandesh/projects/automate_boring_stuff/captcha.jpg text")

with open("text.txt") as captcha:
    captcha = captcha.readline().strip()

driver.find_element_by_id('TextBox1').send_keys(captcha)
driver.find_element_by_id("btnviewresult").click()
