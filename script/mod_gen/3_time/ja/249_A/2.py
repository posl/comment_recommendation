def main():
    A, B, C, D, E, F, X = map(int, input().split())
    Takahashi = (A + C) * (X // (A + C)) + min(A, X % (A + C))
    Aoki = (D + F) * (X // (D + F)) + min(D, X % (D + F))
    Takahashi *= B
    Aoki *= E
    print("Takahashi" if Takahashi > Aoki else "Aoki" if Takahashi < Aoki else "Draw")

if __name__ == '__main__':
    main()