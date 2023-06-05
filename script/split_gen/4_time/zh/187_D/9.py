def solve():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        c, d = map(int, input().split())
        a.append(c)
        b.append(d)
    a.sort(reverse=True)
    b.sort(reverse=True)
    ans = 0
    for i in range(n):
        if a[i] > b[i]:
            ans += 1
    print(ans)
