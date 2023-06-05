def problem137_c():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    ans = 0
    cnt = 1
    for i in range(1, n):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    ans += cnt * (cnt - 1) // 2
    print(ans)

if __name__ == '__main__':
    problem137_c()