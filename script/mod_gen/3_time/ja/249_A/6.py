def main():
    A, B, C, D, E, F, X = map(int, input().split())
    Takahashi = (A + B) * (X // (A + B)) + A * (X % (A + B) // A)
    Aoki = (D + E) * (X // (D + E)) + D * (X % (D + E) // D)
    if Takahashi > Aoki:
        print("Takahashi")
    elif Takahashi < Aoki:
        print("Aoki")
    else:
        print("Draw")

if __name__ == '__main__':
    main()