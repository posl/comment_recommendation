def solve(n, a):
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] != a[j]:
                ans += 1
    return ans

if __name__ == '__main__':
    solve()