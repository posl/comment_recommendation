def solve(n):
    if n == 0:
        return 0
    elif n == 1:
        return 2
    elif n == 2:
        return 2
    else:
        for i in range(1, 100000):
            if n <= i**3:
                return i
            else:
                continue

if __name__ == '__main__':
    solve()