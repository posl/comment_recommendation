def main():
    X = int(input())
    year = 0
    money = 100
    while money < X:
        money = money * 1.01
        year += 1
    print(year)

if __name__ == '__main__':
    main()