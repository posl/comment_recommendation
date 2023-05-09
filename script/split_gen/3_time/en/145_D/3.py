def main():
    X, Y = map(int, input().split())
    if X < Y:
        X, Y = Y, X
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    M = X - N
    ans = 1
    for i in range(M):
        ans *= (N + i + 1)
        ans //= (i + 1)
        ans %= 10**9 + 7
    print(ans)
