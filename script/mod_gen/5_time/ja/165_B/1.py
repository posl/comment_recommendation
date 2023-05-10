def main():
    X = int(input())
    money = 100
    year = 0
    while money < X:
        year += 1
        money += money // 100
    print(year)

if __name__ == '__main__':
    main()