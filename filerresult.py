import unicodecsv as csv

def filterresult():
    csvFile = open("bangdiem.csv", "r")
    csvreader = csv.reader(csvFile)

    dictionary = []
    for row in csvreader:
        dictitem = {
            'mamon' : row[0],
            'diem'  : row[1]
        }
        dictionary.append(dictitem)

    newDict = {}

    for element in dictionary:
        if element['mamon'] not in newDict:
            newDict[element['mamon']] = float(element['diem'])
        else:
            if newDict[element['mamon']] < float(element['diem']):
                newDict[element['mamon']] = float(element['diem'])
    return newDict