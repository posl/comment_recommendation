def main():
    A, B, C, D, E, F, X = map(int, input().split())
    Takahashi = (A + C) * (X // (A + C)) + min(A, X % (A + C))
    Aoki = (D + F) * (X // (D + F)) + min(D, X % (D + F))
    if Takahashi * E > Aoki * B:
        print("Takahashi")
    elif Takahashi * E < Aoki * B:
        print("Aoki")
    else:
        print("Draw")

if __name__ == '__main__':
    main()