def solve(k, x):
    # x is the position of black rock
    # k is the number of black rocks
    min = x - k + 1
    max = x + k - 1
    return range(min, max + 1)

if __name__ == '__main__':
    solve()