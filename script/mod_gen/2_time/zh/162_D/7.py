def solve(n, s):
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            k = 2 * j - i
            if k < n:
                if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                    ans += 1
    return ans

if __name__ == '__main__':
    solve()