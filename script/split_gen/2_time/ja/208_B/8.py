def main():
    P = int(input())
    coins = [0] * 10
    for i in range(10):
        coins[i] = factorial(i+1)
    coins.reverse()
    ans = 0
    for c in coins:
        ans += P // c
        P %= c
    print(ans)
