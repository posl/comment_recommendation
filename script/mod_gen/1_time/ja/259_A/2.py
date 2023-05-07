def main():
    N, M, X, T, D = map(int, input().split())
    if M < X:
        print(T + D * (M - X))
    else:
        print(T)

if __name__ == '__main__':
    main()