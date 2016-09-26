from selenium import webdriver
import time
import unicodecsv as csv

# chrome_options = Options()
# chrome_options.add_argument("disable-popup-blocking")
# driver = webdriver.Chrome(chrome_options=chrome_options)      # using Chrome

driver = webdriver.PhantomJS()              # silent browser
url = 'http://sis.hust.edu.vn/ModuleProgram/CourseLists.aspx'
driver.get(url)

csvFile = open("monhoc.csv", "w")
csvwriter = csv.writer(csvFile, dialect="excel", encoding="utf-8")


for j in range(0, 220):
    print j
    element = []
    for i in range(j*20, (j + 1) * 20):
        try:
            element.append(driver.find_element_by_id("MainContent_gvCoursesGrid_DXDataRow" + str(i)).text)
        except:
            break
    for elements in element:
        mamon, str1 = elements.split(" ", 1)
        tenmon, thoiluong, tinchi, tinchihp, trongso = str1.rsplit(" ", 4)
        csvwriter.writerow([j] + [mamon] + [tenmon] + [tinchi] + [tinchihp] + [trongso])
    driver.execute_script("window.open();")
    driver.switch_to.window(driver.window_handles[j+1])
    time.sleep(5)
    driver.get(url)
    time.sleep(5)
    try:
        driver.execute_script("aspxGVPagerOnClick('MainContent_gvCoursesGrid','PN" + str(j+1) + "');")
    except:
        break
    time.sleep(5)

csvFile.close()
print "Completed!"
driver.close()