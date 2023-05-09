def main():
    X, Y = map(int, input().split())
    X, Y = max(X, Y), min(X, Y)
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    M = X - N
    if M < 0:
        print(0)
        return
    MOD = 10**9 + 7
    ans = 1
    for i in range(N+1, N+M+1):
        ans = ans * i % MOD
    for i in range(1, M+1):
        ans = ans * pow(i, MOD-2, MOD) % MOD
    print(ans)
