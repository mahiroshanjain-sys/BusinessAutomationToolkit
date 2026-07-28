import csv

def stock_value(filename):
    total = 0
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += int(row["Stock"]) * float(row["Price"])
    return round(total, 2)

def total_stock(filename):
    total = 0
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += int(row["Stock"])
    return total

def highest_stock(filename):
    highest = 0
    item = ""
    with open(filename, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row["Stock"]) > highest:
                highest = int(row["Stock"])
                item = row["Item"]
    return item, highest

def low_stock(filename):
    item = ""
    stock = 999999
    with open(filename, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row["Stock"]) < stock:
                stock = int(row["Stock"])
                item = row["Item"]
    return item, stock

def inventory_items(filename):
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        return sum(1 for row in reader)
