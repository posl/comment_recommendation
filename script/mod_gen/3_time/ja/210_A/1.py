def main():
    N, A, X, Y = map(int, input().split())
    if N <= A:
        print(X * N)
    else:
        print(X * A + Y * (N - A))

if __name__ == '__main__':
    main()