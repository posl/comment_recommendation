def main():
    n, m = map(int, input().split())
    x = []
    y = []
    z = []
    for i in range(n):
        a, b, c = map(int, input().split())
        x.append(a)
        y.append(b)
        z.append(c)
    ans = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                s = []
                for l in range(n):
                    s.append(x[l] * (2 * i - 1) + y[l] * (2 * j - 1) + z[l] * (2 * k - 1))
                s.sort(reverse=True)
                ans = max(ans, sum(s[:m]))
    print(ans)
