def main():
    x = int(input())
    year = 0
    money = 100
    while money < x:
        money = money + money // 100
        year = year + 1
    print(year)

if __name__ == '__main__':
    main()