from selenium import webdriver
from selenium.webdriver.common import action_chains, keys
import unicodecsv as csv

driver = webdriver.PhantomJS()

driver.get('http://sis.hust.edu.vn/ModuleUser/vLogin.aspx')
action = action_chains.ActionChains(driver)

secondDriver = webdriver.PhantomJS()
secondDriver.set_window_size(200, 80)
secondDriver.get(driver.find_element_by_id('MainContent_ccCaptcha_IMG').get_attribute('src'))
secondDriver.save_screenshot("captcha.jpg")
secondDriver.close()

driver.find_element_by_id("MainContent_UserName").send_keys(raw_input("Username: "))
driver.find_element_by_id("MainContent_Password").send_keys(raw_input("Password: "))

driver.find_element_by_id("MainContent_ccCaptcha_TB_I").send_keys(raw_input("Captcha: "))

action.send_keys(keys.Keys.ENTER)
action.perform()

driver.get("http://sis.hust.edu.vn/ModuleGradeBook/StudentCourseMarks.aspx")
i=0;
element = []
while True:
    try:
        element.append(driver.find_element_by_id("MainContent_gvCourseMarks_DXDataRow" + str(i)).text)
        i = i + 1;
    except:
        break

csvFile = open("bangdiem.csv", "w")
csvwriter = csv.writer(csvFile, dialect="excel", encoding="utf-8")
for elements in element:
    hocki, mamon, str2 = elements.split(" ", 2)
    tenmon, malop, giuaki, cuoiki, diem = str2.rsplit(" ", 4)
    def f(diem):
        return {
            'A+' : 4,
            'A'  : 4,
            'B+' : 3.5,
            'B'  : 3,
            'C+' : 2.5,
            'C'  : 2,
            'D+' : 1.5,
            'D'  : 1,
            'F'  : 0,
        }.get(diem, 0)
    # csvwriter.writerow([hocki] + [mamon] + str2.rsplit(" ", 4) + [f(diem)])
    csvwriter.writerow([mamon] + [f(diem)])
csvFile.close()

driver.close()