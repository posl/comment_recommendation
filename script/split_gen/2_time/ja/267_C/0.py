def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(m):
        ans += (i + 1) * a[i]
    tmp = ans
    for i in range(n - m):
        tmp = tmp - a[i] + a[i + m]
        ans = max(ans, tmp)
    print(ans)
