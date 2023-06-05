def solve(n, k, a):
    ans = 0
    if (n - k) % (k - 1) == 0:
        ans = (n - k) // (k - 1)
    else:
        ans = (n - k) // (k - 1) + 1
    return ans + 1

if __name__ == '__main__':
    solve()