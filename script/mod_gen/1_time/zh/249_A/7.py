def main():
    A, B, C, D, E, F, X = map(int, input().split())
    Takahashi = 0
    Aoki = 0
    time = 0
    while time < X:
        if Takahashi == Aoki:
            Takahashi += B * A
            Aoki += D * E
            time += A + C
        elif Takahashi > Aoki:
            Aoki += D * E
            time += D + F
        else:
            Takahashi += B * A
            time += A + C
    if Takahashi == Aoki:
        print("DRAW")
    elif Takahashi > Aoki:
        print("AOKI")
    else:
        print("TAKAHASHI")

if __name__ == '__main__':
    main()