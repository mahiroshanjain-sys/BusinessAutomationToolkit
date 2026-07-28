
from utilities.employee import *
basic = 50000
experience = 6
age = 28
gross = calculate_salary(basic)
print("Employee Details")
print("-" * 30)
print("Basic Salary :", basic)
print("Gross Salary :", gross)
print("Bonus :", calculate_bonus(basic, experience))
print("Tax :", calculate_tax(gross))
print("Net Salary :", calculate_net_salary(gross))
print("Annual Salary :", annual_salary(gross))
print("Age :", employee_age(age))
print("Experience :", experience_years(experience))
print("Senior Employee :", is_senior_employee(experience))
print("Years to Retirement :", retirement_years(age))





