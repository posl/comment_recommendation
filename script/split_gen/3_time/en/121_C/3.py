def main():
    n, m = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    c = [a[i] * b[i] for i in range(n)]
    d = sorted(zip(a, b, c))
    ans = 0
    for i in range(n):
        if m <= d[i][1]:
            ans += d[i][0] * m
            break
        else:
            ans += d[i][2]
            m -= d[i][1]
    print(ans)
