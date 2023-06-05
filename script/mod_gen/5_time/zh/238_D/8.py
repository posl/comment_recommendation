def solve(a, s):
    if a > s:
        return False
    if (s - a) % 2 == 0:
        return True
    return False

if __name__ == '__main__':
    solve()