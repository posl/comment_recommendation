def get_price(age, price):
    if age >= 13:
        return price
    elif age >= 6 and age <= 12:
        return price / 2
    else:
        return 0

if __name__ == '__main__':
    get_price()