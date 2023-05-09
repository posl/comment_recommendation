def main():
    P = int(input())
    coins = [1]
    for i in range(1, 11):
        coins.append(coins[i-1] * i)
    coins.reverse()
    ans = 0
    for coin in coins:
        ans += P // coin
        P %= coin
    print(ans)
