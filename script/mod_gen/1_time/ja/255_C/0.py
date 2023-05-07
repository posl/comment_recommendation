def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(abs(X - A))
        return
    if X == A:
        print(0)
        return
    if X < A:
        if D < 0:
            if X < A + D * (N - 1):
                print(abs(X - A))
            else:
                print(abs(X - (A + D * (N - 1))))
        else:
            print(abs(X - A))
    else:
        if D > 0:
            if X > A + D * (N - 1):
                print(abs(X - (A + D * (N - 1))))
            else:
                print(abs(X - A))
        else:
            print(abs(X - A))

if __name__ == '__main__':
    main()