def solve(n,s):
    ans = ''
    for i in range(n):
        if i % 2 == 0:
            ans += s[i]
        else:
            if s[i] == '"':
                ans += '"'
            else:
                ans += '.'
    return ans

if __name__ == '__main__':
    solve()