def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    ans = 0
    for i in range(60):
        c0 = 0
        c1 = 0
        for a in A:
            if a & (1 << i) == 0:
                c0 += 1
            else:
                c1 += 1
        ans += (1 << i) * c0 * c1 % mod
        ans %= mod
    print(ans)
