import getpass
import time
import os
from selenium import webdriver
import unicodecsv as csv
def getmark():
    driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
    url = 'http://sis.hust.edu.vn'
    driver.get(url)

    driver.execute_script("window.open();")
    driver.switch_to.window(driver.window_handles[1])

    time.sleep(5)
    driver.get(url)
    driver.find_element_by_id("cLogIn1_tb_cLogIn_User_I").send_keys(raw_input("Username: "))
    driver.find_element_by_id("cLogIn1_tb_cLogIn_Pass_I").send_keys(getpass.getpass())
    driver.find_element_by_xpath('//*[@id="cLogIn1_bt_cLogIn_B"]').click()

    driver.get("http://sis.hust.edu.vn/ModuleGradeBook/StudentCourseMarks.aspx")
    csvFile = open("bangdiem.csv", "w")
    csvwriter = csv.writer(csvFile, dialect="excel", encoding="utf-8")
    i = 0;
    while True:
        element = []
        try:
            element.append(driver.find_element_by_id("MainContent_gvCourseMarks_DXDataRow" + str(i)).text)
            for elements in element:
                hocki, mamon, str2 = elements.split(" ", 2)
                tenmon, malop, giuaki, cuoiki, diem = str2.rsplit(" ", 4)
                def f(diem):
                    return {
                        'A+': 4,
                        'A': 4,
                        'B+': 3.5,
                        'B': 3,
                        'C+': 2.5,
                        'C': 2,
                        'D+': 1.5,
                        'D': 1,
                        'F': 0,
                    }.get(diem, 0)
                csvwriter.writerow([mamon] + [f(diem)] + [tenmon])
            i = i + 1;
        except:
            break

    csvFile.close()
    driver.close()
