def problems164_c():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    ans = 0
    for i in range(n):
        if i == 0 or s[i] != s[i-1]:
            ans += 1
    print(ans)
