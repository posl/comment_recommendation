def solve(h):
    res = 0
    while h > 0:
        res += h
        h //= 2
    return res

if __name__ == '__main__':
    solve()