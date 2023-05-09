def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        print(abs(X - A))
        return
    if D > 0:
        if X < A:
            print(A - X)
            return
        if X > A + (N - 1) * D:
            print(X - (A + (N - 1) * D))
            return
        print(0)
        return
    if X > A:
        print(X - A)
        return
    if X < A + (N - 1) * D:
        print(abs(X - (A + (N - 1) * D)))
        return
    print(0)

if __name__ == '__main__':
    main()