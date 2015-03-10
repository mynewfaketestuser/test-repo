import csv
with open('./yea.csv', newline='') as file:
    reader = csv.DictReader(file)
    type(reader)
