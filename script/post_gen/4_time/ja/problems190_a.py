Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if c == 0:
        if a > b:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if a < b:
            print("Aoki")
        else:
            print("Takahashi")

=======
Suggestion 3

def main():
    a,b,c = map(int, input().split())
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
Suggestion 4

def main():
    a,b,c = map(int, input().split())
    if c == 0:
        if a > b:
            print('Takahashi')
        else:
            print('Aoki')
    else:
        if b > a:
            print('Aoki')
        else:
            print('Takahashi')

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    if c == 0:
        if a == b:
            print("Aoki")
        elif a > b:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if a == b:
            print("Takahashi")
        elif a > b:
            print("Takahashi")
        else:
            print("Aoki")

=======
Suggestion 6

def main():
    a,b,c = map(int, input().split())
    if c == 0:
        if a > b:
            print('Takahashi')
        else:
            print('Aoki')
    else:
        if a >= b:
            print('Takahashi')
        else:
            print('Aoki')

=======
Suggestion 7

def main():
    # input
    A, B, C = map(int, input().split())

    # compute
    if C == 0:
        if A > B:
            result = "Takahashi"
        else:
            result = "Aoki"
    else:
        if B > A:
            result = "Aoki"
        else:
            result = "Takahashi"

    # output
    print(result)

=======
Suggestion 8

def main():
    #input
    a,b,c = map(int, input().split())
    #compute
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
    #output
