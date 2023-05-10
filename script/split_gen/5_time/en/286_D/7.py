def main():
    N, X = map(int, input().split())
    coins = []
    for _ in range(N):
        A, B = map(int, input().split())
        coins.append((A, B))
    coins.sort()
    ans = 0
    for A, B in coins:
        ans += A * B
        if ans > X * 100:
            print('No')
            return
    print('Yes')
