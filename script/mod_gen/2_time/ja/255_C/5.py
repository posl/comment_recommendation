def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        print(abs(X - A))
        return
    if D > 0:
        if X <= A:
            print(A - X)
            return
        if X < A + D * (N - 1):
            print(0)
            return
        print(X - A - D * (N - 1))
        return
    if D < 0:
        if X >= A:
            print(X - A)
            return
        if X > A + D * (N - 1):
            print(0)
            return
        print(A + D * (N - 1) - X)
        return

if __name__ == '__main__':
    main()