def problem():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        if a[i] > 0:
            b.append(a[i])
    b.sort()
    b.reverse()
    ans = 0
    for i in range(m):
        ans += b[i] * (i + 1)
    print(ans)
problem()

if __name__ == '__main__':
    problem()