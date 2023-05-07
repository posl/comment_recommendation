def jog(A, B, C, D, E, F, X):
    i = 0
    j = 0
    while i < X:
        i += A
        j += B
        i += C
    i = 0
    k = 0
    while i < X:
        i += D
        k += E
        i += F
    if j > k:
        print('Takahashi')
    elif j < k:
        print('Aoki')
    else:
        print('Draw')
