def solve(n, w, a):
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                if a[i] + a[j] + a[k] <= w:
                    ans += 1
                else:
                    break
    return ans

if __name__ == '__main__':
    solve()