def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    return round(amount - principal, 2)

def emi(principal, annual_rate, years):
    monthly_rate = annual_rate / (12 * 100)
    months = years * 12
    emi = principal * monthly_rate * (1 + monthly_rate) ** months
    emi /= ((1 + monthly_rate) ** months - 1)
    return round(emi, 2)

def gst(amount, percent):
    return round(amount * percent / 100, 2)

def discount(amount, percent):
    return round(amount - (amount * percent / 100), 2)
