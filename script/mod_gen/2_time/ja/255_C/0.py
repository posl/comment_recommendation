def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(abs(X - A))
        return
    elif D > 0:
        if X < A:
            print(A - X)
            return
        elif X >= A + D * (N - 1):
            print(X - (A + D * (N - 1)))
            return
        else:
            i = (X - A) // D
            if (X - A) % D == 0:
                print(0)
                return
            else:
                print(min(abs(X - (A + D * i)), abs(X - (A + D * (i + 1)))))
                return
    elif D < 0:
        if X > A:
            print(X - A)
            return
        elif X <= A + D * (N - 1):
            print(abs(X - (A + D * (N - 1))))
            return
        else:
            i = (X - A) // D
            if (X - A) % D == 0:
                print(0)
                return
            else:
                print(min(abs(X - (A + D * i)), abs(X - (A + D * (i - 1)))))
                return

if __name__ == '__main__':
    main()