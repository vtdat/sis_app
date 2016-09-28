import filerresult
import unicodecsv as csv
import urllib2
def calmark():
    bangdiem = filerresult.filterresult()
    url = 'https://raw.githubusercontent.com/vtdat/sis_app/master/monhoc.csv'
    response = urllib2.urlopen(url)
    csvreader = csv.reader(response)
    monhoc = {}
    for row in csvreader:
        monhoc[row[1]] = {
            'tinchi' : row[3],
            'trongso' : row[5]
        }

    listindex = dict.keys(bangdiem)

    newmonhoc = {}
    for index in listindex:
        if index in monhoc:
            newmonhoc[index] = monhoc[index]

    totalmark = float(0)
    totalcredit = float(0)

    for index in listindex:
        totalmark += float(bangdiem[index]) * float(monhoc[index]['tinchi'])
        totalcredit += float(monhoc[index]['tinchi'])
    try:
        cpa = round(totalmark, 2)/round(totalcredit, 2)
    except:
        cpa = -1
    return round(cpa, 2)