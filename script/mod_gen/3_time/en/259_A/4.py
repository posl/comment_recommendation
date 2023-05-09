def main():
    N, M, X, T, D = map(int, input().split())
    if M < X:
        print(T + D * (N - X))
    else:
        print(T + D * (N - M - 1))

if __name__ == '__main__':
    main()