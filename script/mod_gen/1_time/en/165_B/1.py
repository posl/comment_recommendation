def main():
    X = int(input())
    years = 0
    balance = 100
    while balance < X:
        balance = int(balance * 1.01)
        years += 1
    print(years)

if __name__ == '__main__':
    main()