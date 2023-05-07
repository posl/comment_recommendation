def solve(n, k, d, a):
    if k == 1:
        for i in range(n):
            if a[i] % d == 0:
                return a[i]
        return -1
    if d == 1:
        return sum(a)
    if k == 2:
        ans = -1
        for i in range(n):
            for j in range(i+1, n):
                if (a[i] + a[j]) % d == 0:
                    ans = max(ans, a[i] + a[j])
        return ans
    if k == 3:
        ans = -1
        for i in range(n):
            for j in range(i+1, n):
                for l in range(j+1, n):
                    if (a[i] + a[j] + a[l]) % d == 0:
                        ans = max(ans, a[i] + a[j] + a[l])
        return ans

if __name__ == '__main__':
    solve()