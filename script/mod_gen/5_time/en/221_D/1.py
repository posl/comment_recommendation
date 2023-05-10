def solve():
    from collections import defaultdict
    N = int(input())
    d = defaultdict(int)
    for _ in range(N):
        a, b = map(int, input().split())
        d[a] += 1
        d[a+b] -= 1
    d = sorted(d.items())
    ans = [0] * (N+1)
    for i in range(1, len(d)):
        ans[d[i-1][1]] += d[i][0] - d[i-1][0]
    print(*ans[1:])

if __name__ == '__main__':
    solve()