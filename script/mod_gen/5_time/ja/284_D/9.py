def solve(n):
    for i in range(2, n):
        if n % i == 0:
            return i, n // i
    return None

if __name__ == '__main__':
    solve()