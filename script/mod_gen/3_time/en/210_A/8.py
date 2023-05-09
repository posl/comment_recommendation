def main():
    #N, A, X, Y = map(int, input().split())
    #print(N, A, X, Y)
    N, A, X, Y = 5, 3, 20, 15
    if N <= A:
        print(N * X)
    else:
        print(A * X + (N - A) * Y)

if __name__ == '__main__':
    main()