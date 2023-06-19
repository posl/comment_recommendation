def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    # print(d)
    ans = 0
    for i in d:
        ans += d[i] * (d[i] - 1) * (d[i] - 2) // 6
    for i in range(n):
        ans -= (d[a[i]] - 1) * (d[a[i]] - 2) // 2
    print(ans)
