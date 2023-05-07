def main():
    x = int(input())
    year = 0
    balance = 100
    while balance < x:
        balance = balance * 101 // 100
        year += 1
    print(year)

if __name__ == '__main__':
    main()