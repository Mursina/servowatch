import csv

input_file = "test3/sales_data.csv"
output_file = "test3/filtered-sales-data.csv"

data = []
with open(input_file, "r", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

