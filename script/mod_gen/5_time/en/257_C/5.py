def solve(n, s, w):
    ans = 0
    for i in range(n):
        if s[i] == '0':
            ans += w[i]
    ans2 = ans
    for i in range(n):
        if s[i] == '1':
            ans2 += w[i]
    return max(ans, ans2)

if __name__ == '__main__':
    solve()