Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if (a + b) % 2 == 0:
        print((a + b) // 2)
    else:
        print('IMPOSSIBLE')

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if (A + B) % 2 == 0:
        print((A + B) // 2)
    else:
        print('IMPOSSIBLE')

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    if (A + B) % 2 == 0:
        print(int((A + B) / 2))
    else:
        print("IMPOSSIBLE")
    return

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    K = (A + B) // 2
    if abs(A - K) == abs(B - K):
        print(K)
    else:
        print("IMPOSSIBLE")

=======
Suggestion 5

def main():
    a,b = map(int, input().split())
    if (a+b)%2 != 0:
        print("IMPOSSIBLE")
    else:
        print((a+b)//2)

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print((a+b)//2 if (a+b)%2 == 0 else "IMPOSSIBLE")

=======
Suggestion 7

def solve():
    a, b = map(int, input().split())
    if (a+b)%2 != 0:
        print("IMPOSSIBLE")
    else:
        print((a+b)//2)

=======
Suggestion 8

def main():
    #input
    a,b = map(int, input().split())
    #output
    if (a+b)%2 == 0:
        print((a+b)//2)
    else:
        print('IMPOSSIBLE')

=======
Suggestion 9

def main():
    import sys
    import math

    # A, B = input().split()
    A, B = map(int, input().split())

    # print(A, B)

    # print(type(A), type(B))
    # print(A, B)

    # print(type(A), type(B))
    # prin
