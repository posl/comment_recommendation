def main():
    P = int(input())
    coins = [1]
    for i in range(2, 11):
        coins.append(coins[-1]*i)
    ans = 0
    for i in range(len(coins)-1, -1, -1):
        ans += P//coins[i]
        P %= coins[i]
    print(ans)
