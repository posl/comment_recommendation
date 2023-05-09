def main():
    P = int(input())
    coins = [1]
    for i in range(2, 11):
        coins.append(coins[-1] * i)
    coins.reverse()
    count = 0
    for coin in coins:
        count += P // coin
        P %= coin
    print(count)

if __name__ == '__main__':
    main()