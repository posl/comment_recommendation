def solve(n, k):
    if k % 2 == 0:
        a = n // k
        b = (n + k // 2) // k
        return a * a * a + b * b * b
    else:
        a = n // k
        return a * a * a

if __name__ == '__main__':
    solve()