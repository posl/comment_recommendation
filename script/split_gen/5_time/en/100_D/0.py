def main():
    n, m = map(int, input().split())
    x, y, z = [], [], []
    for i in range(n):
        a, b, c = map(int, input().split())
        x.append(a)
        y.append(b)
        z.append(c)
    ans = 0
    for i in range(1 << 3):
        x1, y1, z1 = [], [], []
        for j in range(n):
            if i & 1:
                x1.append(x[j])
            else:
                x1.append(-x[j])
            if i & 2:
                y1.append(y[j])
            else:
                y1.append(-y[j])
            if i & 4:
                z1.append(z[j])
            else:
                z1.append(-z[j])
        x1.sort(reverse=True)
        y1.sort(reverse=True)
        z1.sort(reverse=True)
        ans = max(ans, sum(x1[:m]) + sum(y1[:m]) + sum(z1[:m]))
    print(ans)
