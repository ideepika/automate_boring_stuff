from selenium import webdriver
import base64
from os import system
import time
from selenium.common.exceptions import NoAlertPresentException


def get_roll():
    global current_roll
    return_value = current_roll
    current_roll = current_roll[ :-2] + str(int(current_roll[-2:]) + 1).zfill(2)
    return return_value


def enter_captcha():
    captcha = get_captcha_string("//*[@id='pnlCaptcha']/table/tbody/tr[1]/td/div/img", driver)
    # entering captcha
    driver.find_element_by_id('TextBox1').send_keys(captcha.upper())

    # captcha must be filled after 10 seconds
    time.sleep(5)

    # click viewResult button
    driver.find_element_by_id("btnviewresult").click()
    
    try:
        alrt = driver.switch_to_alert()
        if alrt.text == "you have entered a wrong text":
            alrt.accept()
            driver.find_element_by_xpath('//*[@id="TextBox1"]').clear()
            enter_captcha()
        else :
            alrt.accept()
            driver.find_element_by_xpath("//*[@id='btnReset']").click()
            view_result(get_roll() , semester)
    except NoAlertPresentException as e: 
        print("no alert")
    


def view_result(roll_number, sem):
    try:
        # entering roll no.
        text_area = driver.find_element_by_id('txtrollno')
        text_area.send_keys(str(roll_number))

        # select semester
        driver.find_element_by_xpath("//select[@id='drpSemester']/option[@value='"+str(sem)+"']").click()
    
        enter_captcha()
        
        # deepika's function will be here
        print(roll_number)
        name = driver.find_element_by_xpath("//*[@id='lblNameGrading']")
        print(name.text)
        marks = driver.find_element_by_xpath("//*[@id='lblSGPA']")
        print(marks.text)
        pass_status = driver.find_element_by_xpath("//*[@id='lblResultNewGrading']")
        print(pass_status.text)
  


        driver.find_element_by_xpath("//*[@id='btnReset']").click()
        view_result(get_roll() , semester)
    except:
        global driver
        driver.quit()
        driver = webdriver.Chrome('/home/sandesh/projects/automate_boring_stuff/chromedriver')
        start_chrome()
        view_result(roll_number, sem)


def get_captcha_string(xpath, driver):
    """
    This function takes xpath of the captcha element and chromedriver,
    and returns the string.
    this requires 'tesseract' to be installed in the system
     """
    # find the captcha element
    ele_captcha = driver.find_element_by_xpath(xpath)

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

    # save the captcha to a file captcha.jpg
    with open(r"captcha.jpg", 'wb') as f:
        f.write(base64.b64decode(img_captcha_base64))

    # cracking captha with tesseract (installed on ubuntu 16.04) and saving to text.text
    system("tesseract -l eng /home/sandesh/projects/automate_boring_stuff/captcha.jpg text")

    # reading captcha from text.txt 
    with open("text.txt") as captcha:
        captcha = captcha.readline().strip()
    return captcha


def start_chrome():
    # to go to jec result page
    driver.get("http://www.jecjabalpur.ac.in/Exam/Programselect.aspx")
    sbox = driver.find_element_by_xpath("//input[@id='radlstProgram_0']").click()


current_roll = raw_input("Enter first roll no. ")
semester = int(raw_input("enter semester in integer: "))
# Create a new instance of the chrome driver
driver = webdriver.Chrome('/home/sandesh/projects/automate_boring_stuff/chromedriver')
start_chrome()
view_result(get_roll(), semester)
# driver.execute_script("window.history.go(-1)")
