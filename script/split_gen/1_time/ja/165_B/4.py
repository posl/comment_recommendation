def main():
    # input
    X = int(input())
    # compute
    money = 100
    year = 0
    while money < X:
        money += money // 100
        year += 1
    # output
    print(year)
