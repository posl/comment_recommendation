def solve(a, s):
    if a > s:
        return False
    elif a == s:
        return True
    elif s % 2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    solve()