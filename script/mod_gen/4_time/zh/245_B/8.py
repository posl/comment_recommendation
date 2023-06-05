def solve(n, a):
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] > ans:
            return ans
        elif a[i] == ans:
            ans += 1
    return ans

if __name__ == '__main__':
    solve()