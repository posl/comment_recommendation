def main():
    A, B, C, D, E, F, X = map(int, input().split())
    Takahashi = (B * (X // (A + C)) + B * (X % (A + C)) // A)
    Aoki = (E * (X // (D + F)) + E * (X % (D + F)) // D)
    if Takahashi > Aoki:
        print("Takahashi")
    elif Takahashi < Aoki:
        print("Aoki")
    else:
        print("Draw")

if __name__ == '__main__':
    main()