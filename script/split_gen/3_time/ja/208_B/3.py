def main():
    p = int(input())
    coins = [1]
    for i in range(2,11):
        coins.append(coins[i-2]*i)
    coins.reverse()
    ans = 0
    for coin in coins:
        ans += p // coin
        p %= coin
    print(ans)
