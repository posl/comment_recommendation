def solve(a, n):
    x = 1
    ret = 0
    while x < n:
        x *= a
        ret += 1
    if x == n:
        return ret
    else:
        return -1

if __name__ == '__main__':
    solve()