def main():
    N, A, X, Y = map(int, input().split())
    if N > A:
        print(X*A + Y*(N-A))
    else:
        print(X*N)

if __name__ == '__main__':
    main()