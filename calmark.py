import filerresult
import unicodecsv as csv

def calmark():
    bangdiem = filerresult.filterresult()
    csvFile = open("monhoc.csv", "r")
    csvreader = csv.reader(csvFile)
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

    cpa = round(totalmark, 2)/round(totalcredit, 2)
    return round(cpa, 2)