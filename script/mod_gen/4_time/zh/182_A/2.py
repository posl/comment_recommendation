def solve(a, b):
    if a == 0:
        return 0
    if a == 1:
        return 100
    return 2 * a - b

if __name__ == '__main__':
    solve()