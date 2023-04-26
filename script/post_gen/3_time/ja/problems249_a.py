Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, C, D, E, F, X = map(int, input().split())
    Takahashi = 0
    Aoki = 0
    for i in range(X):
        if i % (A + C) < A:
            Takahashi += B
        if i % (D + F) < D:
            Aoki += E
    if Takahashi > Aoki:
        print('Takahashi')
    elif Aoki > Takahashi:
        print('Aoki')
    else:
        print('Draw')

=======
Suggestion 2

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

=======
Suggestion 3

def main():
    A, B, C, D, E, F, X = map(int, input().split())
    Takahashi = (A + C) * (X // (A + C)) + min(A, X % (A + C))
    Aoki = (D + F) * (X // (D + F)) + min(D, X % (D + F))
    Takahashi *= B
    Aoki *= E
    print("Takahashi" if Takahashi > Aoki else "Aoki" if Takahashi < Aoki else "Draw")

=======
Suggestion 4

def main():
    A, B, C, D, E, F, X = map(int, input().split())
    T = 0
    Aoki = 0
    Takahashi = 0
    while T < X:
        T += A
        Takahashi += B
        T += C
        T += D
        Aoki += E
        T += F
    if Takahashi > Aoki:
        print("Takahashi")
    elif Takahashi < Aoki:
        print("Aoki")
    else:
        print("Draw")

=======
Suggestion 5

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

=======
Suggestion 6

def jog(a, b, c, d, e, f, x):
    takahashi = 0
    aoki = 0
    for i in range(x):
        if i % (a + c) < a:
            takahashi += b
        if i % (d + f) < d:
            aoki += e
    if takahashi > aoki:
        print('Takahashi')
    elif takahashi < aoki:
        print('Aoki')
    else:
        print('Draw')

=======
Suggestion 7

def main():
    A, B, C, D, E, F, X = map(int, input().split())
    Takahashi = (A + B) * (X // (A + B)) + A * (X % (A + B) // A)
    Aoki = (D + E) * (X // (D + E)) + D * (X % (D + E) // D)
    if Takahashi > Aoki:
        print("Takahashi")
    elif Takahashi < Aoki:
        print("Aoki")
    else:
        print("Draw")

=======
Suggestion 8

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

=======
Suggestion 9

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

=======
Suggestion 10

def main():
    #入力
    A, B, C, D, E, F, X = map(int, input().split())
    #高橋君の距離
    Takahashi = (A + C) * (X // (A + C)) + min(A, X % (A + C))
    #青木君の距離
    Aoki = (D + F) * (X // (D + F)) + min(D, X % (D + F))
    #出力
    if Takahashi > Aoki:
        print("Takahashi")
    elif Takahashi < Aoki:
        print("Aoki")
    else:
        print("Draw")
