def solve(a, b, k):
    if a >= k:
        a -= k
    else:
        b -= (k - a)
        a = 0
        if b < 0:
            b = 0
    return a, b

if __name__ == '__main__':
    solve()