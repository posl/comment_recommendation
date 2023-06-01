Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c = map(int, input().split())
    if a**2 + b**2 < c**2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if a**2+b**2 < c**2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    while True:
        try:
            a, b, c = map(int, input().split())
            if a**2 + b**2 < c**2:
                print('Yes')
            else:
                print('No')
        except:
            break

=======
Suggestion 4

def main():
    A,B,C = map(int,input().split())
    if A**2+B**2<C**2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def square():
    A, B, C = input().split()
    A = int(A)
    B = int(B)
    C = int(C)
    if A ** 2 + B ** 2 < C ** 2:
        print('Yes')
    else:
        print('No')
