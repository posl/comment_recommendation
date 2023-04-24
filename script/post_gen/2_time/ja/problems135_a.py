Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if (A + B) % 2 == 0:
        print((A + B) // 2)
    else:
        print("IMPOSSIBLE")

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    K = (A + B) // 2
    if abs(A - K) == abs(B - K):
        print(K)
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

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if (a + b) % 2 == 0:
        print((a + b) // 2)
    else:
        print('IMPOSSIBLE')

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if (a + b) % 2 == 1:
        print("IMPOSSIBLE")
    else:
        print((a + b) // 2)

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    k = (a + b) // 2
    if abs(a-k) == abs(b-k):
        print(k)
    else:
        print("IMPOSSIBLE")

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    if (b - a) % 2 == 0:
        print((b + a) // 2)
    else:
        print("IMPOSSIBLE")

=======
Suggestion 8

def main():
    A, B = map(int, input().split())
    K = (A + B) // 2
    if A == B:
        print(K)
    else:
        print("IMPOSSIBLE")
