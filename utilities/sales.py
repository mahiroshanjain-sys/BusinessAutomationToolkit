import csv

def total_sales(filename):
    total = 0
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += int(row["Quantity"]) * float(row["Price"])
    return round(total, 2)

def average_sales(filename):
    total = 0
    count = 0
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += int(row["Quantity"]) * float(row["Price"])
            count += 1
    return round(total / count, 2)

def highest_sale(filename):
    highest = 0
    product = ""
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            sale = int(row["Quantity"]) * float(row["Price"])
            if sale > highest:
                highest = sale
                product = row["Product"]
    return product, highest

def lowest_sale(filename):
    lowest = None
    product = ""
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            sale = int(row["Quantity"]) * float(row["Price"])
            if lowest is None or sale < lowest:
                lowest = sale
                product = row["Product"]
    return product, lowest

def total_products(filename):
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        return sum(1 for row in reader)
