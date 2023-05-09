def main():
    P = int(input())
    coin = [1]
    for i in range(1, 10):
        coin.append(coin[i-1] * (i+1))
    ans = 0
    for i in range(9, -1, -1):
        ans += P // coin[i]
        P = P % coin[i]
    print(ans)
