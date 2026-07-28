from utilities.employee import calculate_salary, calculate_bonus
from utilities.sales import total_sales
from utilities.finance import emi
from utilities.analytics import growth_rate
from utilities.inventory import stock_value

print("=" * 50)
print("BUSINESS AUTOMATION TOOLKIT")
print("=" * 50)

salary = calculate_salary(50000)
print("\nEmployee")
print("Gross Salary :", salary)
print("Bonus :", calculate_bonus(50000, 7))

print("\nSales")
print("Total Sales :", total_sales(r"C:\Users\Mahi\Desktop\python studies\BusinessAutomationToolkit\data\sales.csv"))

print("\nFinance")
print("Monthly EMI :", emi(2500000, 8.5, 20))

print("\nAnalytics")
print("Growth Rate :", growth_rate(500000, 620000))

print("\nInventory")
print("Inventory Value :", stock_value(r"C:\Users\Mahi\Desktop\python studies\BusinessAutomationToolkit\data\inventory.csv"))

print("\nProject Executed Successfully.")























