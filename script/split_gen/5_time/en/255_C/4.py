def solve():
    X, A, D, N = map(int, input().split())
    if D == 0:
        if X == A:
            return 0
        else:
            return N
    else:
        if (X - A) % D == 0 and (X - A) // D >= 0:
            return min((X - A) // D, N)
        else:
            return N
print(solve())
