Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if c == 0:
        if a > b:
            print('Takahashi')
        else:
            print('Aoki')
    else:
        if a < b:
            print('Aoki')
        else:
            print('Takahashi')

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if c == 0:
        if a > b:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if a >= b:
            print("Takahashi")
        else:
            print("Aoki")

=======
Suggestion 3

def main():
    # input
    A, B, C = map(int, input().split())

    # compute

    # output
    if C == 0:
        if A > B:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if A >= B:
            print("Takahashi")
        else:
            print("Aoki")

=======
Suggestion 4

def main():
    a,b,c = map(int,input().split())
    if c == 0:
        if a > b:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if b > a:
            print("Aoki")
        else:
            print("Takahashi")

=======
Suggestion 5

def main():
    A,B,C=map(int,input().split())
    if A>B:
        print("Takahashi")
    elif A<B:
        print("Aoki")
    else:
        if C==0:
            print("Aoki")
        else:
            print("Takahashi")

=======
Suggestion 6

def main():
    #input
    A, B, C = map(int, input().split())
    #compute
    if C == 0:
        if A > B:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if A >= B:
            print("Takahashi")
        else:
            print("Aoki")
    #output
