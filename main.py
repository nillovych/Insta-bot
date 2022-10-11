import pyperclip
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from fake_useragent import UserAgent
import random
from subprocess import call
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
#proxy

from proxy_auth import login,password

#captcha_libs

from python_anticaptcha import AnticaptchaClient, ImageToTextTask
import urllib.request


#email csv
df = pd.read_csv('gmail.csv')
df1 = pd.DataFrame(df, columns= ['username','firstname','lastname'])
#динамічна зміна номеру пошти з кожною ітерацією


useragent = UserAgent()

options = webdriver.ChromeOptions()

options.add_argument(f"user-agent={useragent.random}")
#options.add_argument(f"80.244.235.205:1256")

#proxy_smart
#proxy_options = {
    #"proxy" : {
        

        #"https" : f"https://mt_4:mt_49595@76.170.38.226:8094"
    #}
#}

browser = webdriver.Chrome(
    options = options,
    #seleniumwire_options = proxy_options
    
)

browser.get('https://appleid.apple.com/account')

inputs = browser.find_elements_by_tag_name('input')

selectors = browser.find_elements_by_tag_name('select') 

#inputs
firstname_input = inputs[4]    
lastname_input = inputs[5]
date_birth_input = inputs[6]
email_input = inputs[7]
pass_input = inputs[8]
pass_prove_input = inputs[9]
phone_num_input = inputs[10]
captcha_input = inputs[15]

#list of names
#my_first = ['Liam', 'Noah', 'Oliver', 'Elijah', 'William', 'James', 'Benjamin', 'Lucas', 'Henry', 'Alexander']
#my_last = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia','Miller', 'Davis', 'Rodriguez', 'Martinez']

bot_name = df1['firstname'][0]
print(bot_name)

firstname_input.send_keys(bot_name)
lastname_input.send_keys(df1['lastname'][0])

ctry_reg = selectors[0]
phone_num = selectors[1]

ctry_regDD = Select(ctry_reg)
ctry_regDD.select_by_value("USA")

month_m = ['01','02','03','04','05','06','07','08','09','10','11']
days_d = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20']
years_y = ['1999','2000','2001','2002']

bot_year_birth = random.choice(years_y)

date_birth = random.choice(days_d) + random.choice(month_m) + bot_year_birth
date_birth_input.send_keys(date_birth)

#password
password = ''
for x in range(3): 
    password = password + random.choice(list('abcdefghigklmnopqrstuvyxwz'))+ random.choice(list('ABCDEFGHIGKLMNOPQRSTUVYXWZ')) + random.choice(list('1234567890'))


print(password)

pass_input.send_keys(password)
pass_prove_input.send_keys(password)

#email

email_input.send_keys(df1['username'][0])

#captcha

img = browser.find_elements_by_tag_name('img')
src = img[0].get_attribute('src')

urllib.request.urlretrieve(src, "captcha.png")

api_key = '08d0fa50ed1d8e68fd01ce4f37fbd71f'
client = AnticaptchaClient(api_key)

img_file = open('captcha.png', 'rb')
task = ImageToTextTask(img_file)
job = client.createTask(task)
job.join()

solution = job.get_captcha_text()

captcha_input.send_keys(solution)







