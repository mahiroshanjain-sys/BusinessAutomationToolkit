from utilities.sales import *

file = r"C:\Users\Mahi\Desktop\python studies\BusinessAutomationToolkit\data\sales.csv"

print("=" * 40)
print("SALES REPORT")
print("=" * 40)

print("Total Sales :", total_sales(file))
print("Average Sales :", average_sales(file))

product, sale = highest_sale(file)
print("Highest Sale Product :", product)
print("Highest Sale Amount :", sale)

product, sale = lowest_sale(file)
print("Lowest Sale Product :", product)
print("Lowest Sale Amount :", sale)

print("Products Available :", total_products(file))
