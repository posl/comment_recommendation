def main():
    n = int(input())
    a, p, x = [], [], []
    for i in range(n):
        ai, pi, xi = map(int, input().split())
        a.append(ai)
        p.append(pi)
        x.append(xi)
    ans = 10**9+1
    for i in range(n):
        if x[i] > a[i]:
            ans = min(ans, p[i])
    if ans == 10**9+1:
        ans = -1
    print(ans)
