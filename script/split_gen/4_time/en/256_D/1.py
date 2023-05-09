def solve():
    n = int(input())
    intervals = []
    for _ in range(n):
        l, r = map(int, input().split())
        intervals.append((l, r))
    intervals.sort(key=lambda x: x[0])
    ans = []
    l, r = intervals[0]
    for i in range(1, n):
        nl, nr = intervals[i]
        if r < nl:
            ans.append((l, r))
            l, r = nl, nr
        else:
            r = max(r, nr)
    ans.append((l, r))
    for l, r in ans:
        print(l, r)
