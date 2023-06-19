def main():
    x = int(input())
    money = 100
    year = 0
    while money < x:
        year += 1
        money = money * 1.01 // 1
    print(year)

if __name__ == '__main__':
    main()