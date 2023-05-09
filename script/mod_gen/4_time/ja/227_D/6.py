def solve(n, k, a):
    a.sort(reverse=True)
    return sum(a[:k])

if __name__ == '__main__':
    solve()