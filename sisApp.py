# coding=utf-8
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import unicodecsv as csv
import os

class sisApp():
    def __init__(self):
        global url
        global driver
        url = 'http://sis.hust.edu.vn'

        driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
        # chrome_options = Options()
        # chrome_options.add_argument("disable-popup-blocking")
        # driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(url)

    def login(self, username = None, password = None):
        if username == None or password == None:
            return False
        else:
            try:
                driver.get(url)
                driver.find_element_by_id("cLogIn1_tb_cLogIn_User_I").send_keys(username)
                driver.find_element_by_id("cLogIn1_tb_cLogIn_Pass_I").send_keys(password)
                driver.find_element_by_xpath('//*[@id="cLogIn1_bt_cLogIn_B"]').click()
                try:
                    wait = WebDriverWait(driver, 5)
                    wait.until(lambda driver: driver.find_element_by_xpath('//*[@id="site_header"]/table/tbody/tr/td[3]/p'))
                    if u'Xin chào bạn' in driver.find_element_by_xpath('//*[@id="site_header"]/table/tbody/tr/td[3]/p').text:
                        return True
                except TimeoutException:
                    if u'sis.hust.edu.vn/ModuleUser/vLogin.aspx' in driver.title:
                        return False
                    else:
                        self.login(username, password)
            except:
                self.login(username, password)

    @staticmethod
    def _convertmark (mark):
        return {'A+': 4,'A': 4,'B+': 3.5,'B': 3,'C+': 2.5,'C': 2,'D+': 1.5,'D': 1,'F': 0}.get(mark, 0)

    def getmark(self, export = 0):
        driver.get(url + '/ModuleGradeBook/StudentCourseMarks.aspx')
        if u'403' in driver.title:
            driver.get(url + '/ModuleGradeBook/StudentCourseMarks.aspx')
        result = []
        i = 0
        while True:
            elements = []
            try:
                elements.append(driver.find_element_by_id("MainContent_gvCourseMarks_DXDataRow" + str(i)).text)
                for element in elements:
                    semester, subjcode, ranstring = element.split(" ", 2)
                    subjname, credit, classcode, midterm, final, mark = ranstring.rsplit(" ", 5)
                    if not classcode:
                        classcode = credit
                        subjname, credit = subjname.rsplit(" ", 1)
                    result.append({'semester' : semester, 'subjcode' : subjcode, 'subjname' : subjname,
                                   'credit' : credit, 'mark' : self._convertmark(mark)})
                i += 1
            except:
                break
        if export == 1:
            csvfile = open("bangdiem.csv", 'w')
            csvwriter = csv.writer(csvfile, dialect='excel', encoding='utf-8')
            for item in result:
                csvwriter.writerow([unicode(item['semester'])] + [unicode(item['subjcode'])] + [unicode(item['subjname'])] + [unicode(item['credit'])] + [unicode(item['mark'])])
            csvfile.close()
        return result

    def getcpa(self):
        subjects = []
        totalmark = float(0)
        totalcredit = float(0)
        if os.path.isfile("bangdiem.csv"):
            csvFile = open("bangdiem.csv", "r")
            csvreader = csv.reader(csvFile)

            for row in csvreader:
                dictitem = {'subjcode':row[1],'mark':row[4], 'credit':row[3]}
                subjects.append(dictitem)
        else:
            allsubjects = self.getmark()
            for subject in allsubjects:
                subjects.append({'subjcode':subject['subjcode'], 'mark':subject['mark'], 'credit':subject['credit']})

        subjects = self._filterredudant(subjects)
        for item in subjects:
            totalcredit += float(subjects[item]['credit'])
            totalmark += float(subjects[item]['credit']) * float(subjects[item]['mark'])
        try:
            cpa = totalmark/totalcredit
        except:
            return False
        return round(cpa, 2)

    def _filterredudant(self, data):
        result = {}
        for element in data:
            if element['subjcode'] not in result:
                result[element['subjcode']] = {'mark' : float(element['mark']), 'credit':element['credit']}
            else:
                if result[element['subjcode']]['mark'] < float(element['mark']):
                    result[element['subjcode']]['mark'] = float(element['mark'])
        return result

    def close(self):
        driver.delete_all_cookies()
        driver.close()