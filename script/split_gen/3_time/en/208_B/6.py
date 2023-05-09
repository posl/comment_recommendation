def main():
    p = int(input())
    coins = [0] * 10
    for i in range(1, 11):
        coins[i-1] = i * (i + 1) // 2
    coins.reverse()
    ans = 0
    for i in range(10):
        ans += p // coins[i]
        p %= coins[i]
    print(ans)
