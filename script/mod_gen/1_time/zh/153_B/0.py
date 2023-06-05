def solve(h, a):
    if h <= 0:
        return True
    if len(a) == 0:
        return False
    t = a.pop()
    return solve(h, a) or solve(h-t, a)

if __name__ == '__main__':
    solve()