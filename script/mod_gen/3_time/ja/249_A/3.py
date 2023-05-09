def main():
    A, B, C, D, E, F, X = map(int, input().split())
    T = 0
    Aoki = 0
    Takahashi = 0
    while T < X:
        T += A
        Takahashi += B
        T += C
        T += D
        Aoki += E
        T += F
    if Takahashi > Aoki:
        print("Takahashi")
    elif Takahashi < Aoki:
        print("Aoki")
    else:
        print("Draw")

if __name__ == '__main__':
    main()