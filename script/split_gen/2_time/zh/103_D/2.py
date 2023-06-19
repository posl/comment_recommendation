def main():
    n, m = map(int, input().split())
    a = [0 for i in range(m)]
    b = [0 for i in range(m)]
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    a.sort()
    b.sort()
    ans = 0
    for i in range(m):
        if i == 0:
            ans = a[0] - 1
        else:
            ans += a[i] - a[i-1] - 1
        if i == m - 1:
            ans += n - b[-1]
    print(ans)
