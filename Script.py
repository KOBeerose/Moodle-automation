import time
import string
from datetime import datetime, timedelta
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.support.ui import Select



# !!!!! this script is meant to work on Moodle platform but you can make changes use it with another one !!!! 


# today's date
sdate = (datetime.now()).strftime('%d/%m/%Y')



u_name= "user" # defining Username
u_password= "password" # defining getting password


# configuration and direction to the website URL 
url= "http://m.inpt.ac.ma/login/index.php"
options = EdgeOptions()
options.use_chromium= True
driver = Edge(options=options)
driver.get(url)




# entering user's Name and Password and clicking the join now button
user_name = driver.find_element_by_name("username")
user_name.send_keys(u_name)

user_password = driver.find_element_by_name("password")
user_password.send_keys(u_password)

outside = driver.find_element_by_id("rememberusername")
outside.click()

outside = driver.find_element_by_id("loginbtn")
outside.click()


