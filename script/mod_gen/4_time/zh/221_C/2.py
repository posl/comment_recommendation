def solve(n):
    n = str(n)
    ans = 0
    for i in range(1, len(n)):
        a = int(n[:i])
        b = int(n[i:])
        ans = max(ans, a * b)
    return ans

if __name__ == '__main__':
    solve()