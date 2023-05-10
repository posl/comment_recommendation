def solve(x, y, z):
    if x < z:
        return -1
    return (x - z) - y

if __name__ == '__main__':
    solve()