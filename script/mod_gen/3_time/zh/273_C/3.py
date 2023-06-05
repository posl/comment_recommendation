def solve(n, a):
    a.sort()
    s = set()
    ans = [0] * n
    for i in range(n-1, -1, -1):
        x = a[i]
        if x in s:
            ans[i] = ans[i+1]
        else:
            s.add(x)
            ans[i] = ans[i+1] + 1
    return ans

if __name__ == '__main__':
    solve()