def main():
    A, B, C, D, E, F, X = map(int, input().split())
    Takahashi = (A + C) * (X // (A + C)) + B * min(X % (A + C), A)
    Aoki = (D + F) * (X // (D + F)) + E * min(X % (D + F), D)
    if Takahashi > Aoki:
        print('Takahashi')
    elif Takahashi < Aoki:
        print('Aoki')
    else:
        print('Draw')

if __name__ == '__main__':
    main()