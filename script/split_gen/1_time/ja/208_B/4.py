def main():
    P = int(input())
    coins = [1]
    for i in range(2, 11):
        coins.append(coins[-1] * i)
    ans = 0
    for i in range(10, 0, -1):
        ans += P // coins[i-1]
        P %= coins[i-1]
    print(ans)
