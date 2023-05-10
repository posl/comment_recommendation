def main():
    A,B,C,D,E,F,X = map(int, input().split())
    Aoki = Takahashi = 0
    if A > 0:
        Takahashi += B
    if D > 0:
        Aoki += E
    for i in range(1, X):
        if i % (A + C) < A:
            Takahashi += B
        if i % (D + F) < D:
            Aoki += E
    if Takahashi > Aoki:
        print('Takahashi')
    elif Takahashi < Aoki:
        print('Aoki')
    else:
        print('Draw')

if __name__ == '__main__':
    main()