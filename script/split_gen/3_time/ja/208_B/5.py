def main():
    P = int(input())
    coin = [1]
    for i in range(2, 11):
        coin.append(coin[-1] * i)
    ans = 0
    for i in range(10, 0, -1):
        ans += P // coin[i - 1]
        P %= coin[i - 1]
    print(ans)
