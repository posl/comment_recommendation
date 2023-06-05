def pay(coin, price):
    if coin == 0:
        return False
    if coin == 1:
        return price == 0
    if coin == 2:
        return price % 2 == 0
    if coin == 5:
        return price % 5 == 0
    if coin == 10:
        return price % 10 == 0
    if coin == 50:
        return price % 50 == 0
    if coin == 100:
        return price % 100 == 0
    if coin == 500:
        return price % 500 == 0
    if coin == 1000:
        return price % 1000 == 0
    return False

if __name__ == '__main__':
    pay()