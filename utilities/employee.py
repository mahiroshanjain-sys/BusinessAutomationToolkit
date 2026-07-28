from datetime import datetime

def calculate_salary(basic_salary):
    hra = basic_salary * 0.20
    da = basic_salary * 0.10
    total = basic_salary + hra + da
    return round(total, 2)

def calculate_bonus(basic_salary, experience):
    if experience >= 10:
        bonus = basic_salary * 0.20
    elif experience >= 5:
        bonus = basic_salary * 0.10
    else:
        bonus = basic_salary * 0.05
    return round(bonus, 2)

def calculate_tax(gross_salary):
    return round(gross_salary * 0.10, 2)

def calculate_net_salary(gross_salary):
    tax = calculate_tax(gross_salary)
    return gross_salary - tax

def employee_age(age):
    return age

def experience_years(exp):
    return exp

def annual_salary(monthly_salary):
    return monthly_salary * 12

def monthly_salary(annual):
    return annual / 12

def is_senior_employee(exp):
    return exp >= 8

def retirement_years(age):
    return 60 - age












