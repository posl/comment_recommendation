def cost(age, price):
    if age >= 13:
        return price
    elif age >= 6:
        return price//2
    else:
        return 0

if __name__ == '__main__':
    cost()