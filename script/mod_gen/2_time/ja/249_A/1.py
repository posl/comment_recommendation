def main():
    A, B, C, D, E, F, X = map(int, input().split())
    Takahashi = 0
    Aoki = 0
    for i in range(X):
        if i % (A + C) < A:
            Takahashi += B
        if i % (D + F) < D:
            Aoki += E
    if Takahashi > Aoki:
        print("Takahashi")
    elif Takahashi < Aoki:
        print("Aoki")
    else:
        print("Draw")

if __name__ == '__main__':
    main()