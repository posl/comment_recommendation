def main():
    p = int(input())
    coins = [1]
    for i in range(1, 11):
        coins.append(coins[-1] * (i+1))
    coins.reverse()
    ans = 0
    for coin in coins:
        ans += p // coin
        p %= coin
    print(ans)
