def main():
    n = int(input())
    a = []
    p = []
    x = []
    for i in range(n):
        ai, pi, xi = map(int, input().split())
        a.append(ai)
        p.append(pi)
        x.append(xi)
    ans = -1
    for i in range(n):
        if x[i] > 0:
            if ans == -1:
                ans = p[i]
            else:
                ans = min(ans, p[i])
    print(ans)
