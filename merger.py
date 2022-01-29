import csv
from email import header

dataSet1 = []
dataSet2 = []

with open('stars1.csv') as f:
    csv_reader = csv.reader(f)
    for rows in csv_reader:
        dataSet1.append(rows)

with open('star2.csv') as f:
    csv_reader = csv.reader(f)
    for rows in csv_reader:
        dataSet2.append(rows)

header1 = dataSet1[0]
header2 = dataSet2[0]

planet_data1 = dataSet1[1:]
planet_data2 = dataSet2[1:]

headers = header1 + header2

planet_data = []

for index,data in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])

