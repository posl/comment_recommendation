def solve():
    X, A, D, N = map(int, input().split())
    if D == 0:
        if X == A:
            return 0
        else:
            return 1
    if N == 1:
        if A == X:
            return 0
        else:
            return 1
    if D > 0:
        if X <= A:
            return 1
        else:
            return 1 + (X - A) // D
    else:
        if X >= A:
            return 1
        else:
            return 1 + (A - X) // (-D)
print(solve())

if __name__ == '__main__':
    solve()