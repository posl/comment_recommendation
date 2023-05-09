def main():
    N = int(input())
    x = []
    y = []
    p = []
    for _ in range(N):
        xi, yi, pi = map(int, input().split())
        x.append(xi)
        y.append(yi)
        p.append(pi)
    ans = 1
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if p[i] * ans >= abs(x[i] - x[j]) + abs(y[i] - y[j]):
                ans += 1
                break
    print(ans)
