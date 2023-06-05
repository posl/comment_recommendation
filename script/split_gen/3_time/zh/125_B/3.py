def solve():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0
    for i in range(1 << n):
        x = 0
        y = 0
        for j in range(n):
            if i & (1 << j):
                x += v[j]
                y += c[j]
        ans = max(ans, x - y)
    print(ans)
