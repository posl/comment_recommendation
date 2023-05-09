def main():
    N, M, X, T, D = map(int, input().split())
    print(T + (M - X) * D if M > X else T)

if __name__ == '__main__':
    main()