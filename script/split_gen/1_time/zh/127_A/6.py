def calcPrice(age, price):
    if age >= 13:
        return price
    elif age >= 6 and age <= 12:
        return price / 2
    else:
        return 0
