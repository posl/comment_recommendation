def main():
    N, M, X, T, D = map(int, input().split())
    if N <= X:
        print(T + D * (N - 1))
    else:
        print(T + D * (X - 1) + (N - X))

if __name__ == '__main__':
    main()