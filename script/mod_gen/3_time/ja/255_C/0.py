def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(abs(X - A))
    else:
        if D > 0:
            if X < A:
                print(abs(X - A))
            elif X > A + D * (N - 1):
                print(abs(X - (A + D * (N - 1))))
            else:
                print(min(abs(X - A), abs(X - (A + D * (N - 1)))))
        else:
            if X > A:
                print(abs(X - A))
            elif X < A + D * (N - 1):
                print(abs(X - (A + D * (N - 1))))
            else:
                print(min(abs(X - A), abs(X - (A + D * (N - 1)))))

if __name__ == '__main__':
    main()