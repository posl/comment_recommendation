def main():
    x = int(input())
    money = 100
    year = 0
    while money < x:
        money += money//100
        year += 1
    print(year)

if __name__ == '__main__':
    main()