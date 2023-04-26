Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    K = (A + B) // 2
    if abs(A - K) == abs(B - K):
        print(K)
    else:
        print("IMPOSSIBLE")

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if (A + B) % 2 == 0:
        print((A + B) // 2)
    else:
        print("IMPOSSIBLE")

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if (a + b) % 2 == 0:
        print((a + b) // 2)
    else:
        print("IMPOSSIBLE")

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    if (A + B) % 2 == 0:
        print((A + B) // 2)
    else:
        print('IMPOSSIBLE')

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    if (A + B) % 2 == 0:
        print(int((A + B) / 2))
    else:
        print("IMPOSSIBLE")

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    if (A + B) % 2 == 1:
        print("IMPOSSIBLE")
    else:
        print((A + B) // 2)

=======
Suggestion 7

def solve():
    A, B = map(int, input().split())
    K = (A + B) // 2
    if (A - K) == (B - K):
        print(K)
    else:
        print("IMPOSSIBLE")

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    if (a + b) % 2 == 1:
        print("IMPOSSIBLE")
    else:
        print((a+b)//2)

=======
Suggestion 9

def main():
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    if (b - a) % 2:
        print("IMPOSSIBLE")
    else:
        print((a + b) // 2)
