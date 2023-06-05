def solve(a, b, c, k):
    if a >= k:
        return k
    elif a + b >= k:
        return a
    else:
        return a - (k - a - b)

if __name__ == '__main__':
    solve()