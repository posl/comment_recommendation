def main():
    X = int(input())
    money = 100
    year = 0
    while money < X:
        money += money // 100
        year += 1
    print(year)

if __name__ == '__main__':
    main()