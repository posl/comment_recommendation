def solve(a, s):
    if a > s:
        return False
    if a == s:
        return True
    if a == 0:
        return False
    if a & 1 == 0:
        return solve(a >> 1, s >> 1)
    else:
        return solve(a >> 1, s >> 1) or solve(a >> 1, (s >> 1) + 1)

if __name__ == '__main__':
    solve()