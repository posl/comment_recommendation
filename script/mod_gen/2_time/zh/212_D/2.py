def solve(n, m, a, b):
    a.sort()
    b.sort()
    ans = 10 ** 9
    j = 0
    for i in range(n):
        while j + 1 < m and b[j + 1] < a[i]:
            j += 1
        ans = min(ans, abs(a[i] - b[j]))
    return ans

if __name__ == '__main__':
    solve()