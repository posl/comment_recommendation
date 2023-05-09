def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    if X > N or Y > N:
        print(0)
        return
    mod = 10 ** 9 + 7
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % mod
    inv = [1] * (N + 1)
    inv[N] = pow(fact[N], mod - 2, mod)
    for i in range(N, 0, -1):
        inv[i - 1] = inv[i] * i % mod
    print(fact[N] * inv[X] % mod * inv[Y] % mod)
