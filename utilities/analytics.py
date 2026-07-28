def percentage(obtained, total):
    return round((obtained / total) * 100, 2)

def growth_rate(previous, current):
    return round(((current - previous) / previous) * 100, 2)

def profit_margin(revenue, profit):
    return round((profit / revenue) * 100, 2)

def profit(revenue, expense):
    return revenue - expense

def loss(revenue, expense):
    if expense > revenue:
        return expense - revenue
    return 0
