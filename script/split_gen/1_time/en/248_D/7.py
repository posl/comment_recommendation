def solve():
    from collections import Counter
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())
    queries = []
    for _ in range(Q):
        L, R, X = [int(x) for x in input().split()]
        queries.append((L, R, X))
    count = Counter(A)
    ans = []
    for L, R, X in queries:
        ans.append(count[X])
    print(*ans, sep='
')
solve()
