def solve(n, s):
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = r * g * b
    for i in range(n):
        for j in range(i+1, n):
            k = 2 * j - i
            if k >= n:
                continue
            if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
                ans -= 1
    return ans

if __name__ == '__main__':
    solve()