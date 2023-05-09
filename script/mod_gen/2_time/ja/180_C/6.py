def solve(n):
    res = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res.add(i)
            res.add(n // i)
    return sorted(res)

if __name__ == '__main__':
    solve()