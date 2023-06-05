def solve():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    res = 0
    for i in range(n):
        if m >= ab[i][0]:
            res += ab[i][1]
            m -= 1
    print(res)
