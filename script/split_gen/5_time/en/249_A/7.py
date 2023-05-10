def solve():
    A,B,C,D,E,F,X = map(int, input().split())
    Takahashi = 0
    Aoki = 0
    for i in range(X):
        if i % (A+B) < A:
            Takahashi += C
        if i % (D+E) < D:
            Aoki += F
    if Takahashi > Aoki:
        print('Takahashi')
    elif Aoki > Takahashi:
        print('Aoki')
    else:
        print('Draw')
