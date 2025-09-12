import csv

file = "/Users/kashifmaqbool/Python for AI/5_Python_Beta_Part2/5.1reg_no.csv"

with open(file, 'r') as f:
    reader = csv.reader(f)

    header = next(reader)
    print(header)

    for row in reader:
        print(row)