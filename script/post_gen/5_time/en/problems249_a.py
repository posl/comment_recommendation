Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C, D, E, F, X = map(int, input().split())
    Takahashi = 0
    Aoki = 0
    for i in range(1, X+1):
        if (i % (A+B)) <= A:
            Takahashi += C
        if (i % (D+E)) <= D:
            Aoki += F
    if Takahashi > Aoki:
        print("Takahashi")
    elif Takahashi < Aoki:
        print("Aoki")
    else:
        print("Draw")

=======
Suggestion 2

def main():
    A, B, C, D, E, F, X = map(int, input().split())
    Takahashi = 0
    Aoki = 0
    while X > 0:
        if Takahashi + B * A >= Aoki + D * E:
            Takahashi += B * A
            X -= A
            if X <= 0:
                break
            else:
                X -= C
        else:
            Aoki += D * E
            X -= D
            if X <= 0:
                break
            else:
                X -= F
    if Takahashi > Aoki:
        print("Takahashi")
    elif Takahashi < Aoki:
        print("Aoki")
    else:
        print("Draw")

=======
Suggestion 3

def main():
    # input
    A, B, C, D, E, F, X = map(int, input().split())

    # compute

    # output
    if (A * B) > (D * E):
        print("Takahashi")
    elif (A * B) < (D * E):
        print("Aoki")
    else:
        print("Draw")

=======
Suggestion 4

def main():
    a,b,c,d,e,f,x = map(int, input().split())
    t = 0
    aoki = 0
    takahashi = 0
    while t < x:
        if t % (a + b) < a:
            takahashi += c
        if t % (d + e) < d:
            aoki += f
        t += 1
    if takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")
    else:
        print("Draw")

=======
Suggestion 5

def main():
    a,b,c,d,e,f,x = map(int,input().split())
    takahashi = 0
    aoki = 0
    for i in range(x):
        if i % (a + b) < a:
            takahashi += c
        if i % (d + e) < d:
            aoki += f
    if takahashi > aoki:
        print('Takahashi')
    elif takahashi < aoki:
        print('Aoki')
    else:
        print('Draw')

=======
Suggestion 6

def main():
    a, b, c, d, e, f, x = map(int, input().split())
    tak = 0
    aok = 0
    for i in range(1, x+1):
        if i % (a + b + c) <= a:
            tak += 1
        if i % (d + e + f) <= d:
            aok += 1
    if tak > aok:
        print('Takahashi')
    elif tak < aok:
        print('Aoki')
    else:
        print('Draw')

=======
Suggestion 7

def main():
    A,B,C,D,E,F,X = map(int, input().split())
    Takahashi = A * B
    Aoki = D * E
    if Takahashi > Aoki:
        print("Takahashi")
    elif Takahashi < Aoki:
        print("Aoki")
    else:
        print("Draw")

=======
Suggestion 8

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

=======
Suggestion 9

def main():
    a,b,c,d,e,f,x = map(int,input().split())
    t = 0
    aoki = 0
    takahashi = 0
    while(t<x):
        if(t%2==0):
            takahashi += a
        else:
            aoki += d
        t += 1
    if(takahashi > aoki):
        print("Takahashi")
    elif(takahashi < aoki):
        print("Aoki")
    else:
        print("Draw")
