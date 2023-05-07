def solve():
    n = int(input())
    x, y, p = [], [], []
    for i in range(n):
        a, b, c = map(int, input().split())
        x.append(a)
        y.append(b)
        p.append(c)
    
    ans = 0
    for i in range(n):
        for j in range(n):
            if p[i] * ans >= abs(x[i] - x[j]) + abs(y[i] - y[j]):
                ans = max(ans, (abs(x[i] - x[j]) + abs(y[i] - y[j]) + p[j] - 1) // p[j])
    
    print(ans)
