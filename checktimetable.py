from sisApp import *

app = sisApp('', '')
app.login()
driver = app.getdriver()
driver.get('http://sis.hust.edu.vn/ModulePlans/Timetables.aspx')
username = app.getusername()

def fill():
    driver.find_element_by_id('MainContent_Studentid_I').send_keys(username)
    driver.find_element_by_id('MainContent_btFind_B').click()
    wait = WebDriverWait(driver, 5)
    try:
        wait.until(lambda driver: driver.find_element_by_id('MainContent_lbStatus'))
    except:
        driver.get('http://sis.hust.edu.vn/ModulePlans/Timetables.aspx')
        fill()
    if '403' in driver.title:
        driver.get('http://sis.hust.edu.vn/ModulePlans/Timetables.aspx')
        fill()
    elif unicode(username) not in driver.find_element_by_id('MainContent_lbStatus').text:
        driver.get('http://sis.hust.edu.vn/ModulePlans/Timetables.aspx')
        fill()
    else:
        return True
fill()

result = []
i = 0
while True:
    elements = []
    try:
        elements.append(driver.find_element_by_id("MainContent_gvStudentRegister_DXDataRow" + str(i)).text)
        for element in elements:
            print element
        i += 1
    except:
        break