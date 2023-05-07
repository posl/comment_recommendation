def main():
    from sys import stdin
    from math import ceil
    readline = stdin.readline
    N, M = map(int, readline().split())
    A = list(map(int, readline().split()))
    B = sorted([a - i for i, a in enumerate(A, 1)], reverse=True)
    ans = 0
    for i in range(M):
        ans += ceil(B[i] / M)
    print(ans)
