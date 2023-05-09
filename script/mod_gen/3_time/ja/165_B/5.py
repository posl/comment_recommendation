def main():
    X = int(input())
    #print(X)
    year = 0
    money = 100
    while money < X:
        money = int(money * 1.01)
        year = year + 1
    print(year)

if __name__ == '__main__':
    main()