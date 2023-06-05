def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    for i in range(q):
        x.append(int(input()))
    a.sort()
    for i in range(q):
        cnt = 0
        for j in range(n):
            if x[i] <= a[j]:
                cnt += 1
        print(cnt)
solve()
