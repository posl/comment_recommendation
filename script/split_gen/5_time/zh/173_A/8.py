def change_money(n):
    money = 1000 - n % 1000
    if money == 1000:
        money = 0
    return money
