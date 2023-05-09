def main():
    x = int(input())
    year = 0
    balance = 100
    while balance < x:
        year += 1
        balance = int(balance * 1.01)
    print(year)

if __name__ == '__main__':
    main()