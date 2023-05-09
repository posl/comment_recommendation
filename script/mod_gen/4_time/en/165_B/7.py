def main():
    # input
    x = int(input())
    # compute
    year = 0
    balance = 100
    while balance < x:
        year += 1
        balance = int(balance * 1.01)
    # output
    print(year)

if __name__ == '__main__':
    main()