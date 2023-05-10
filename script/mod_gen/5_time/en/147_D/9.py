def solve():
    from collections import Counter
    from itertools import accumulate
    MOD = 10**9+7
    N = int(input())
    A = list(map(int, input().split()))
    C = Counter(A)
    C = [v*(N-v) for v in C.values()]
    C = list(accumulate(C))
    ans = 0
    for c in C[:-1]:
        ans += c
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    solve()