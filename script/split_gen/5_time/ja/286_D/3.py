def main():
    N, X = map(int, input().split())
    coins = []
    for _ in range(N):
        coins.append(list(map(int, input().split())))
    coins.sort()
    coins.reverse()
    ans = 0
    for coin in coins:
        if coin[1] > 0:
            ans += coin[0]
            coin[1] -= 1
    if ans >= X:
        print("Yes")
    else:
        print("No")
