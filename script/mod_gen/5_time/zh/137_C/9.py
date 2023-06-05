def solve():
    n = int(input())
    s = [input() for i in range(n)]
    for i in range(n):
        s[i] = ''.join(sorted(s[i]))
    s = sorted(s)
    ans = 0
    cnt = 1
    for i in range(1, n):
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    ans += cnt * (cnt - 1) // 2
    print(ans)

if __name__ == '__main__':
    solve()