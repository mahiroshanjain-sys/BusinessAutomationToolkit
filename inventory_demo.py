from utilities.inventory import *
file = r"C:\Users\Mahi\Desktop\python studies\BusinessAutomationToolkit\data\inventory.csv"
print("=" * 40)
print("INVENTORY REPORT")
print("=" * 40)
print("Inventory Value :", stock_value(file))
print("Total Stock :", total_stock(file))
item, stock = highest_stock(file)
print("Highest Stock :", item, stock)
item, stock = low_stock(file)
print("Lowest Stock :", item, stock)
print("Items :", inventory_items(file))




