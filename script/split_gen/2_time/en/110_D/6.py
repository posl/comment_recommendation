def main():
    import sys
    from collections import defaultdict
    from math import sqrt
    readline = sys.stdin.readline
    mod = 10 ** 9 + 7
    N, M = map(int, readline().split())
    f = defaultdict(int)
    for i in range(2, int(sqrt(M)) + 1):
        while M % i == 0:
            f[i] += 1
            M //= i
    if M > 1:
        f[M] += 1
    ans = 1
    for k, v in f.items():
        ans *= (v + 1) ** N
        ans %= mod
    print(ans)
