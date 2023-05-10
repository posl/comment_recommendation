def solve():
    N = int(input())
    A = list(map(int, input().split()))
    from collections import defaultdict
    d = defaultdict(int)
    for a in A:
        d[a] += 1
    ans = []
    for a in A:
        ans.append(N-1 - (d[a]-1))
    print(*ans)

if __name__ == '__main__':
    solve()