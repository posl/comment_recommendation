def process():
    n, a, b = map(int, input().split())
    s = input()
    ans = 0
    for i in range(n):
        if s[i] == s[n - i - 1]:
            continue
        elif s[i] == 'a':
            ans += a
        elif s[i] == 'b':
            ans += b
        elif s[n - i - 1] == 'a':
            ans += a
        elif s[n - i - 1] == 'b':
            ans += b
        else:
            print(-1)
            return
    if ans % 2 == 0:
        print(ans // 2)
    else:
        print(ans // 2 + 1)
