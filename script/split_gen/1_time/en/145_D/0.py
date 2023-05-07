def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    if N < max(X, Y):
        print(0)
        return
    MOD = 10**9 + 7
    fact = [1]
    for i in range(1, N + 1):
        fact.append((fact[-1] * i) % MOD)
    inv = [pow(fact[-1], MOD - 2, MOD)]
    for i in range(N, 0, -1):
        inv.append((inv[-1] * i) % MOD)
    inv.reverse()
    print((fact[N] * inv[X] * inv[Y]) % MOD)
