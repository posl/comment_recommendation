def main():
    A, B, C, D, E, F, X = map(int, input().split())
    Takahashi = (A + C) * B
    Aoki = D * E
    if X <= Takahashi and X <= Aoki:
        print('Draw')
    elif X <= Takahashi:
        print('Takahashi')
    elif X <= Aoki:
        print('Aoki')
    else:
        print('Draw')

if __name__ == '__main__':
    main()