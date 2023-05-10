def calc(money, discnt):
    for i in range(discnt):
        money = money // 2
    return money

if __name__ == '__main__':
    calc()