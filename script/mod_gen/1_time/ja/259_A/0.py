def main():
    N, M, X, T, D = map(int, input().split())
    if M >= X:
        print(T + (N - M) * D)
    else:
        print(T + (X - M) * D)

if __name__ == '__main__':
    main()