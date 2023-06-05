def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * (n+1)
    for i in range(n):
        b[i+1] = b[i] + a[i]
    d = {}
    for i in range(n+1):
        r = b[i] % m
        if r in d:
            d[r] += 1
        else:
            d[r] = 1
    ans = 0
    for i in d:
        ans += d[i] * (d[i]-1) // 2
    print(ans)
