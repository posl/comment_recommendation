def main():
    A, B, C, D, E, F, X = map(int, input().split())
    T = 0
    Takahashi = 0
    Aoki = 0
    while True:
        if Takahashi > Aoki:
            Aoki += D * E
            T += D
        elif Takahashi

if __name__ == '__main__':
    main()