def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        a[i] %= 200
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    ans = 0
    for i in d:
        ans += d[i] * (d[i] - 1) // 2
    print(ans)
