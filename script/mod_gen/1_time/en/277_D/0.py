def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * m
    for i in range(n):
        b[a[i]] += 1
    for i in range(m):
        b[i] %= 2
    c = []
    for i in range(m):
        if b[i] == 1:
            c.append(i)
    ans = 0
    for i in range(len(c)):
        ans += min(c[i], m-c[i])
    print(ans)
main()
