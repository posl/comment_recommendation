def solve():
    X, A, D, N = map(int, input().split())
    if D == 0:
        if X == A:
            return 0
        else:
            return -1
    if N == 1:
        if X == A:
            return 0
        else:
            return -1
    if N == 2:
        if X == A:
            return 0
        elif X == A + D or X == A - D:
            return 1
        else:
            return -1
    if N % 2 == 0:
        if X % 2 == 0:
            if X % D == 0:
                return 1
            else:
                return 2
        else:
            if (X + D) % D == 0:
                return 2
            else:
                return 3
    else:
        if X % 2 == 0:
            if (X + D) % D == 0:
                return 2
            else:
                return 3
        else:
            if X % D == 0:
                return 1
            else:
                return 2

if __name__ == '__main__':
    solve()