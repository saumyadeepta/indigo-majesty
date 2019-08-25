from selenium import webdriver
chromedriver = "E:/gldrv/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get('https://web.whatsapp.com/')
name=input('enter the name of user or group:')
msg=input('enter your msg:')
count=int(input('enter the count'))

input('enter anything after scanning QR code')
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
msg_box = driver.find_element_by_class_name('_13mgZ')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()
    
