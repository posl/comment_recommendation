def count_coins(p):
    coins = [1]
    for i in range(2, 11):
        coins.append(coins[-1]*i)
    count = 0
    for i in range(9, -1, -1):
        count += p // coins[i]
        p %= coins[i]
    return count
while True:
    try:
        p = int(input())
        print(count_coins(p))
    except:
        break

if __name__ == '__main__':
    count_coins()