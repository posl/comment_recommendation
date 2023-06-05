def solve():
    import sys
    f = open('problems159_d.txt', 'r')
    sys.stdin = f
    N = int(input())
    A = list(map(int, input().split()))
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(N):
        d[A[i]] += 1
    ans = 0
    for k in range(1, N+1):
        ans += d[k] * (d[k] - 1) // 2
    for i in range(N):
        print(ans - (d[A[i]] - 1))

if __name__ == '__main__':
    solve()