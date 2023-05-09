def main():
    # Inputs
    X, A, D, N = map(int, input().split())
    # A + (N-1) * D = X
    # N = (X - A) / D + 1
    # N = (X - A + D) / D
    # N = X // D - A // D + 1
    # N = X // D - A // D + 1
    N = X // D - A // D + 1
    print(N)

if __name__ == '__main__':
    main()