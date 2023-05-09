def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = [0] + a
    for i in range(n):
        a[i + 1] += a[i]
    r = {}
    for i in a:
        r[i % m] = r.get(i % m, 0) + 1
    ans = 0
    for i in r:
        ans += r[i] * (r[i] - 1) // 2
    print(ans)
