import time
import string
from datetime import datetime, timedelta
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.support.ui import Select


# !!!!! this script is meant to work on Moodle platform but you can make changes use it with another one !!!!


# today's date
sdate = (datetime.now()).strftime('%d/%m/%Y')


u_name = "user"  # defining Username
u_password = "password"  # defining getting password

# configuration and direction to the website URL

url_login = "http://m.inpt.ac.ma/login/index.php"
url_calander = "http://calendrier.inpt.ac.ma/CALENDRIER_INE1.pdf"

options = EdgeOptions()
options.use_chromium = True
driver = Edge(options=options)
driver.get(url_login)

# open new window with execute_script()
driver.execute_script("window.open('%s');" % url_calander)


options = EdgeOptions()
options.use_chromium = True

browser = driver.edge(os.getcwd()+'/edge')


pdf_url = browser.find_element_by_tag_name('iframe').get_attribute("src")

browser.get(pdf_url)

download = browser.find_element_by_xpath('//*[@id="download"]')

download.click()
options.add_experimental_option('prefs', {
    # Change default directory for downloads
    "download.default_directory": "C:/Users/tahae/Download",
    "download.prompt_for_download": False,  # To auto download the file
    "download.directory_upgrade": True,
    # It will not show PDF directly in chrome
    "plugins.always_open_pdf_externally": True
})

options.use_chromium = True
driver = Edge(options=options)

# entering user's Name and Password and clicking the join now button
user_name = driver.find_element_by_name("username")
user_name.send_keys(u_name)

user_password = driver.find_element_by_name("password")
user_password.send_keys(u_password)

outside = driver.find_element_by_id("rememberusername")
outside.click()

outside = driver.find_element_by_id("loginbtn")
outside.click()
