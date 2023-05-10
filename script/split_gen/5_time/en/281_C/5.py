def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    t -= 1
    for i in range(1, n):
        a[i] += a[i-1]
    print(t//a[n-1]*n + (next(i for i in range(n) if a[i] > t%a[n-1]) + 1) if t%a[n-1] in a else next(i for i in range(n) if a[i] > t%a[n-1]) + 1, t%a[n-1] if t%a[n-1] in a else t%a[n-1] - a[next(i for i in range(n) if a[i] > t%a[n-1]) - 1])
