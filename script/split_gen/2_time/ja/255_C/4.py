def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        print(abs(X - A))
        return
    if D > 0:
        if X < A:
            print(A - X)
            return
        elif X > A + (N - 1) * D:
            print(X - A - (N - 1) * D)
            return
        else:
            print(min(X - A, A + (N - 1) * D - X))
            return
    else:
        if X > A:
            print(X - A)
            return
        elif X < A + (N - 1) * D:
            print(A + (N - 1) * D - X)
            return
        else:
            print(min(A - X, X - A - (N - 1) * D))
            return
