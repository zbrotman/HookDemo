import csv

file = open('test.txt', 'w')
with open('Test_for_script.csv', 'rb') as csvfile:
    testReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in testReader:
        file.writelines(row)
file.close()

