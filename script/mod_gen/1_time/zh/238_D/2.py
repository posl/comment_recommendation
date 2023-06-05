def solve(a,s):
    if a > s:
        return False
    if a == s:
        return True
    if a & 1 == 1:
        if s & 1 == 1:
            return True
        else:
            return False
    else:
        if s & 1 == 1:
            return False
        else:
            return solve(a>>1,s>>1)

if __name__ == '__main__':
    solve()