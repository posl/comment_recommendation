def solution1():
    n = int(input())
    s = input()
    r = [0 for _ in range(n)]
    g = [0 for _ in range(n)]
    b = [0 for _ in range(n)]
    for i in range(n):
        if s[i] == 'R':
            r[i] += 1
        elif s[i] == 'G':
            g[i] += 1
        else:
            b[i] += 1
    for i in range(1, n):
        r[i] += r[i - 1]
        g[i] += g[i - 1]
        b[i] += b[i - 1]
    ans = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if s[i] == 'R':
                if s[j] == 'G':
                    ans += b[n - 1] - b[j]
                    if j + j - i < n and s[j + j - i] == 'B':
                        ans -= 1
                elif s[j] == 'B':
                    ans += g[n - 1] - g[j]
                    if j + j - i < n and s[j + j - i] == 'G':
                        ans -= 1
            elif s[i] == 'G':
                if s[j] == 'R':
                    ans += b[n - 1] - b[j]
                    if j + j - i < n and s[j + j - i] == 'B':
                        ans -= 1
                elif s[j] == 'B':
                    ans += r[n - 1] - r[j]
                    if j + j - i < n and s[j + j - i] == 'R':
                        ans -= 1
            else:
                if s[j] == 'R':
                    ans += g[n - 1] - g[j]
                    if j + j - i < n and s[j + j - i] == 'G':
                        ans -= 1
                elif s[j] == 'G':
                    ans += r[n - 1] - r[j]
                    if j + j - i < n and s[j + j - i] == 'R':
                        ans -= 1
    print(ans)
