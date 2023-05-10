def calc_year(x):
    year = 0
    money = 100
    while money < x:
        money = int(money * 1.01)
        year += 1
    return year
