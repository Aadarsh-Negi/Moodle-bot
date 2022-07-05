from threading import Thread
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
caps=[{
      'os_version': '10',
      'os': 'Windows',
      'browser': 'chrome',
      'browser_version': '89.0',
      'name': 'Parallel Test1', # test name
      'build': 'browserstack-build-1' # Your tests will be organized within this build
      }]
link = 'your_browserstack_token' #your browserstack token
browser = webdriver.Remote(command_executor=link,desired_capabilities=caps[0])
userN='username' #your username
passwrd='password' #your password
browser.get('http://45.116.207.204/moodle/login/index.php') #server link
username = browser.find_element_by_id('username')
username.send_keys(userN)
pss = browser.find_element_by_id('password')
pss.send_keys(passwrd)

login = browser.find_element_by_id('loginbtn')
login.click()
#subject's attendence page link
subject = ['http://45.116.207.204/moodle/mod/attendance/view.php?id=4137','http://45.116.207.204/moodle/mod/attendance/view.php?id=4075','http://45.116.207.204/moodle/mod/attendance/view.php?id=4111','http://45.116.207.204/moodle/mod/attendance/view.php?id=4080','http://45.116.207.204/moodle/mod/attendance/view.php?id=4103','http://45.116.207.204/moodle/mod/attendance/view.php?id=4132','http://45.116.207.204/moodle/mod/attendance/view.php?id=4173','http://45.116.207.204/moodle/mod/attendance/view.php?id=4175','http://45.116.207.204/moodle/mod/attendance/view.php?id=4200']
def ck():
    try:
        smt = browser.find_element_by_link_text("Submit attendance")
        smt.click()
        radio = browser.find_elements_by_name('status')
        radio[0].click()
        l2=browser.find_element_by_id('id_submitbutton')
        l2.click()
        return 1
    except NoSuchElementException:
        return 0

def submit(lnk):
    browser.get(lnk)
    if ck() == 0:
        return 0
    else:
        return 1
 #main   
for x in subject:
    submit(x)
    

browser.quit()  


