def main():
    n = int(input())
    x = []
    y = []
    for _ in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    xy = list(zip(x, y))
    xy.sort()
    x.sort()
    y.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if x[i] < x[j] and y[i] < y[j]:
                if (x[i], y[j]) in xy and (x[j], y[i]) in xy:
                    ans += 1
    print(ans)
