Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, c, d, e, f, x = map(int, input().split())
    takahashi = (a + c) * (x // (a + c)) + min(a, x % (a + c))
    aoki = (d + f) * (x // (d + f)) + min(d, x % (d + f))
    if takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")
    else:
        print("Draw")

=======
Suggestion 2

def main():
    A, B, C, D, E, F, X = map(int, input().split())
    takahashi = (A + C) * (X // (A + C)) + min(A, X % (A + C))
    aoki = (D + F) * (X // (D + F)) + min(D, X % (D + F))
    if takahashi > aoki:
        print("Takahashi")
    elif aoki > takahashi:
        print("Aoki")
    else:
        print("Draw")

=======
Suggestion 3

def main():
    A, B, C, D, E, F, X = map(int, input().split())
    Takahashi = (A + C) * (X // (A + C)) + min(A, X % (A + C))
    Aoki = (D + F) * (X // (D + F)) + min(D, X % (D + F))
    if Takahashi * E > Aoki * B:
        print("Takahashi")
    elif Takahashi * E < Aoki * B:
        print("Aoki")
    else:
        print("Draw")

=======
Suggestion 4

def main():
    a, b, c, d, e, f, x = map(int, input().split())
    takahashi = (a + c) * (x // (a + c)) + b * (x % (a + c) // a)
    aoki = (d + f) * (x // (d + f)) + e * (x % (d + f) // d)
    if takahashi > aoki:
        print('Takahashi')
    elif takahashi < aoki:
        print('Aoki')
    else:
        print('Draw')

=======
Suggestion 5

def main():
    A, B, C, D, E, F, X = map(int, input().split())
    T = A * B * X // (A * B + C * (X // (A + C)))
    A = X - T
    T = A * B
    A = X - T // (D + E) * D
    T = A * E
    if T > T:
        print("Takahashi")
    elif T < T:
        print("Aoki")
    else:
        print("Draw")

main()

=======
Suggestion 6

def main():
    A, B, C, D, E, F, X = map(int, input().split())
    Takahashi = (B * (X // (A + C)) + B * (X % (A + C)) // A)
    Aoki = (E * (X // (D + F)) + E * (X % (D + F)) // D)
    if Takahashi > Aoki:
        print("Takahashi")
    elif Takahashi < Aoki:
        print("Aoki")
    else:
        print("Draw")

=======
Suggestion 7

def main():
    A,B,C,D,E,F,X = map(int,input().split())
    Takahashi = 0
    Aoki = 0
    Takahashi = (A+B)*C
    Aoki = (D+E)*F
    if Takahashi > Aoki:
        print("Takahashi")
    elif Takahashi < Aoki:
        print("Aoki")
    else:
        print("Draw")

=======
Suggestion 8

def main():
    # A B C D E F X
    a, b, c, d, e, f, x = map(int, input().split())
    # 1 ≦ A, B, C, D, E, F, X ≦ 100
    if 1 <= a <= 100 and 1 <= b <= 100 and 1 <= c <= 100 and 1 <= d <= 100 and 1 <= e <= 100 and 1 <= f <= 100 and 1 <= x <= 100:
        takahashi = 0
        aoki = 0
        for i in range(x):
            if i % (a + c) < a:
                takahashi += b
            if i % (d + f) < d:
                aoki += e
        # print(takahashi, aoki)
        if takahashi > aoki:
            print("Takahashi")
        elif takahashi < aoki:
            print("Aoki")
        else:
            print("Draw")

=======
Suggestion 9

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

=======
Suggestion 10

def main():
    #input
    A, B, C, D, E, F, X = map(int, input().split())
    #compute
    #output
    if (A * B * C) > (D * E * F):
        print("Takahashi")
    elif (A * B * C) < (D * E * F):
        print("Aoki")
    else:
        print("Draw")
