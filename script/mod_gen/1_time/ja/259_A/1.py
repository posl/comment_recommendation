def main():
    N, M, X, T, D = map(int, input().split())
    if M < X:
        print(T + (N - X) * D)
    else:
        print(T)
main()

if __name__ == '__main__':
    main()