def solve():
    N = int(input())
    x = []
    y = []
    p = []
    for i in range(N):
        xi, yi, pi = map(int, input().split())
        x.append(xi)
        y.append(yi)
        p.append(pi)
    ans = 10**9
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            d = abs(x[i] - x[j]) + abs(y[i] - y[j])
            ans = min(ans, d // p[i])
    print(ans)

if __name__ == '__main__':
    solve()