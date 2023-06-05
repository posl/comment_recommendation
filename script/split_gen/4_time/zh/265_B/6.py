def main():
    n, m, t = map(int, input().split())
    a = [int(i) for i in input().split()]
    x = [0] * m
    y = [0] * m
    for i in range(m):
        x[i], y[i] = map(int, input().split())
    for i in range(m):
        a[x[i] - 2] += y[i]
    for i in range(n - 2):
        if t - a[i] <= 0:
            print('No')
            return
        t -= a[i]
    print('Yes')
