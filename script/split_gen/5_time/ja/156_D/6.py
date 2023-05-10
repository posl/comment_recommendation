def main():
    n, a, b = map(int, input().split())
    mod = 10**9 + 7
    if b - a == 1:
        print((pow(2, n, mod) - 1) % mod)
    else:
        print((pow(2, n, mod) - 1 - comb(n, a) - comb(n, b)) % mod)
