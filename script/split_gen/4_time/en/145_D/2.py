def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    if X > N or Y > N:
        print(0)
        return
    MOD = 10**9 + 7
    fact = [0] * (N + 1)
    fact[0] = 1
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv = [0] * (N + 1)
    inv[N] = pow(fact[N], MOD - 2, MOD)
    for i in range(N - 1, -1, -1):
        inv[i] = inv[i + 1] * (i + 1) % MOD
    print(fact[2 * N] * inv[N] * inv[N] % MOD)
