def main():
    x = int(input())
    balance = 100
    years = 0
    while balance < x:
        years += 1
        balance = int(balance * 1.01)
    print(years)

if __name__ == '__main__':
    main()