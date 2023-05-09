def main():
    X = int(input())
    money = 100
    years = 0
    while money < X:
        money = int(money * 1.01)
        years += 1
    print(years)

if __name__ == '__main__':
    main()