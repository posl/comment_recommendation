def solve(L):
    if L == 12:
        return 1
    ans = 0
    for i in range(1, L-10):
        ans += solve(L-i)
    return ans

if __name__ == '__main__':
    solve()