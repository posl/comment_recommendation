def main():
    n, m = map(int, input().split())
    a = list(map(lambda x: int(x) % m, input().split()))
    c = [0] * m
    for i in range(n):
        c[a[i]] += 1
    ans = 0
    for i in range(m):
        if c[i] > 1:
            ans += min(i, m - i) * (c[i] - 1)
    print(ans)
