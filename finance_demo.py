from utilities.finance import *

print("=" * 40)
print("FINANCE REPORT")
print("=" * 40)

print("Simple Interest :", simple_interest(500000, 8, 5))
print("Compound Interest :", compound_interest(500000, 8, 5))
print("Home Loan EMI :", emi(2500000, 8.5, 20))
print("GST :", gst(12000, 18))
print("Discount :", discount(5000, 10))
