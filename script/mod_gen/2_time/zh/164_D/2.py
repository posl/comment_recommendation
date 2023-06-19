def solve(s):
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i+3,n):
            if int(s[i:j+1]) % 2019 == 0:
                ans += 1
    return ans

if __name__ == '__main__':
    solve()