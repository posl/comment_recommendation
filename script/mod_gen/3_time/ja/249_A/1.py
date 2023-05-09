def main():
    A, B, C, D, E, F, X = map(int, input().split())
    takahashi = (A + C) * (X // (A + C)) + min(A, X % (A + C))
    aoki = (D + F) * (X // (D + F)) + min(D, X % (D + F))
    if takahashi * E > aoki * B:
        print('Takahashi')
    elif takahashi * E < aoki * B:
        print('Aoki')
    else:
        print('Draw')

if __name__ == '__main__':
    main()