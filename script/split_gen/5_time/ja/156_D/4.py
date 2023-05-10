def main():
    n, a, b = map(int, input().split())
    mod = 10**9 + 7
    ans = pow(2, n, mod) - 1
    for i in range(a):
        ans -= comb(n, i, mod)
    for i in range(b):
        ans -= comb(n, i, mod)
    print(ans % mod)
