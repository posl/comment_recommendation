def jog(A, B, C, D, E, F, X):
    T = A * B * (X // (A + C)) + B * min(A, X % (A + C))
    A = D * E * (X // (D + F)) + E * min(D, X % (D + F))
    if T > A:
        print("Takahashi")
    elif T < A:
        print("Aoki")
    else:
        print("Draw")
A, B, C, D, E, F, X = map(int, input().split())
jog(A, B, C, D, E, F, X)

if __name__ == '__main__':
    jog()