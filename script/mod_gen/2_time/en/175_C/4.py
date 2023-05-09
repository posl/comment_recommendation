def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    if K * D <= X:
        print(X - K * D)
    else:
        if (K - X // D) % 2 == 0:
            print(X % D)
        else:
            print(abs(X % D - D))

if __name__ == '__main__':
    main()