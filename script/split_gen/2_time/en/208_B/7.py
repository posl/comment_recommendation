def main():
    p = int(input())
    coins = [1]
    for i in range(2,11):
        coins.append(coins[-1]*i)
    coins.reverse()
    count = 0
    for coin in coins:
        count += p//coin
        p %= coin
    print(count)
