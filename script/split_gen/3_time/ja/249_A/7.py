def jog(A, B, C, D, E, F, X):
    takahashi = 0
    aoki = 0
    for i in range(0, X):
        if i % (A + C) < A:
            takahashi += B
        if i % (D + F) < D:
            aoki += E
    if takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")
    else:
        print("Draw")
A, B, C, D, E, F, X = map(int, input().split())
jog(A, B, C, D, E, F, X)
