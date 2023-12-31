import csv

input_file = "test3/sales_data.csv"
output_file = "test3/filtered-sales-data.csv"

data = []
with open(input_file, "r", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

total_price_per_sqft = 0
count = 0

for row in data:
    try:
        price = float(row["price"])
        sqft = float(row["sq__ft"])
        if sqft != 0:  # Avoid division by zero
            price_per_sqft = price / sqft
            total_price_per_sqft += price_per_sqft
            count += 1
    except ValueError:
        continue

average_price_per_sqft = total_price_per_sqft / count

filtered_data = [row for row in data if float(row["sq__ft"]) > 0 and float(row["price"]) / float(row["sq__ft"]) < average_price_per_sqft]

with open(output_file, "w", newline="") as csvfile:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(filtered_data)

print(f"Filtered data saved to {output_file}")