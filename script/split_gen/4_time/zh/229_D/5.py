def solve():
    s = input()
    k = int(input())
    n = len(s)
    a = [0] * n
    for i in range(n):
        if s[i] == 'X':
            a[i] = 1
    b = [0] * n
    b[0] = a[0]
    for i in range(1, n):
        b[i] = b[i - 1] + a[i]
    ans = 0
    for i in range(n):
        if s[i] == 'X':
            ans += 1
            continue
        if i == 0:
            ans = max(ans, b[min(i + k, n - 1)])
        else:
            ans = max(ans, b[min(i + k, n - 1)] - b[i - 1])
    print(ans)
solve()
