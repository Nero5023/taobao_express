from selenium import webdriver
import random
import Configure
import time

driver = webdriver.Chrome()

driver.get(
    "https://login.taobao.com/member/login.jhtml?spm=a2e15.8261149.754894437.1.4d7529b4O4AbNj&f=top&redirectURL=http%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Fkeyword%3D%25E7%25BD%2591%25E6%25B7%2598%25E5%25AE%259D%26refpid%3Dmm_26632258_3504122_32538762%26clk1%3D9ee2d6259e68593095396fa6f91ed469%26upsid%3D9ee2d6259e68593095396fa6f91ed469")

driver.find_element_by_xpath('//*[@id="J_Quick2Static"]').click()

# login
time.sleep(1)
for ch in Configure.USER_NAME:
    time.sleep(random.random())
    driver.find_element_by_id("TPL_username_1").send_keys(ch)

time.sleep(1)

for ch in Configure.PASSWORD:
    time.sleep(random.random())
    driver.find_element_by_id("TPL_password_1").send_keys(ch)

time.sleep(3)
driver.find_element_by_id("J_SubmitStatic").click()

print(driver.get_cookies())

driver.quit()
