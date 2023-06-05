def main():
    x = int(input())
    coin500 = x // 500
    coin5 = (x % 500) // 5
    print(coin500 * 1000 + coin5 * 5)

if __name__ == '__main__':
    main()