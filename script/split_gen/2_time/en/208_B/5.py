def main():
    p = int(input())
    coins = [1]
    for i in range(1, 10):
        coins.append(coins[i-1]*(i+1))
    coins.reverse()
    ans = 0
    for coin in coins:
        ans += p//coin
        p %= coin
    print(ans)
