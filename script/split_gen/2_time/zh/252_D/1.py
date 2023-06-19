def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    s = 0
    for i in d:
        s += d[i] * (d[i] - 1) * (d[i] - 2) // 6
    for i in range(n):
        s -= (d[a[i]] - 1) * (d[a[i]] - 2) // 2
    print(s)
