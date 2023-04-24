Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    if C == 0:
        if A > B:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if B > A:
            print("Aoki")
        else:
            print("Takahashi")

=======
Suggestion 2

def main():
    A, B, C = map(int, input().split())
    if C == 0:
        if A > B:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if B > A:
            print("Aoki")
        else:
            print("Takahashi")
    return

=======
Suggestion 3

def main():
    A, B, C = map(int, input().split())
    if C == 0:
        if A > B:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if B > A:
            print("Aoki")
        else:
            print("Takahashi")

main()

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
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
    a, b, c = map(int, input().split())
    if c == 0:
        a -= 1
    else:
        b -= 1
    if a > b:
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 6

def main():
    a, b, c = map(int, input().split())
    if a > b:
        print('Takahashi')
    elif a < b:
        print('Aoki')
    else:
        if c == 0:
            print('Aoki')
        else:
            print('Takahashi')

main()

=======
Suggestion 7

def main():
    A, B, C = input().split()
    A = int(A)
    B = int(B)
    C = int(C)
    if (C == 0 and A > B) or (C == 1 and A >= B):
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 8

def main():
    A, B, C = map(int, input().split())
    print("Takahashi" if A > B or C == 0 else "Aoki")

=======
Suggestion 9

def main():
    #write your code here
    pass
