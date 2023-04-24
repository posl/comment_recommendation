Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C, D, E, F, X = map(int, input().split())
    takahashi = (A + C) * B
    aoki = D * E
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
    takahashi = (A + C) * B
    aoki = D * E
    if takahashi > aoki:
        print('Takahashi')
    elif takahashi < aoki:
        print('Aoki')
    else:
        print('Draw')

=======
Suggestion 3

def main():
    A, B, C, D, E, F, X = map(int, input().split())
    takahashi = (A + C) * B
    aoki = (D + F) * E
    if takahashi > aoki:
        print("Takahashi")
    elif aoki > takahashi:
        print("Aoki")
    else:
        print("Draw")

=======
Suggestion 4

def main():
    A, B, C, D, E, F, X = map(int, input().split())
    takahashi = A * B + C * B
    aoki = D * E + F * E
    if takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")
    else:
        print("Draw")

=======
Suggestion 5

def main():
    A, B, C, D, E, F, X = map(int, input().split())
    taka = (A + C) * B
    aoki = (D + F) * E
    if taka > aoki:
        print("Takahashi")
    elif taka < aoki:
        print("Aoki")
    else:
        print("Draw")

=======
Suggestion 6

def main():
    a, b, c, d, e, f, x = map(int, input().split())
    takahashi = 0
    aoki = 0
    takahashi = (a + c) * b
    aoki = d * e
    if takahashi == aoki:
        print("Draw")
    elif takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")

main()

=======
Suggestion 7

def main():
    a,b,c,d,e,f,x = map(int, input().split())
    takahashi = (a+c)*b
    aoki = d*e
    if takahashi > aoki:
        print("Takahashi")
    elif aoki > takahashi:
        print("Aoki")
    else:
        print("Draw")

main()

=======
Suggestion 8

def main():
    A,B,C,D,E,F,X = map(int, input().split())
    Takahashi = 0
    Aoki = 0
    for i in range(0,X):
        if i < A:
            Takahashi += B
        elif i >= A and i < A + C:
            Takahashi += 0
        elif i >= A + C:
            Takahashi += B
    for j in range(0,X):
        if j < D:
            Aoki += E
        elif j >= D and j < D + F:
            Aoki += 0
        elif j >= D + F:
            Aoki += E
    if Takahashi > Aoki:
        print("Takahashi")
    elif Takahashi < Aoki:
        print("Aoki")
    else:
        print("Draw")

=======
Suggestion 9

def main():
    # Read input
    A, B, C, D, E, F, X = map(int, input().split())

    # Calculate distance
    takahashi = (A + C) * B
    aoki = D * E

    # Print output
    if takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")
    else:
        print("Draw")
