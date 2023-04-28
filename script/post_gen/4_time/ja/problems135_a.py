Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if (a + b) % 2 == 0:
        print(int((a + b) / 2))
    else:
        print("IMPOSSIBLE")
    return

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if (a + b) % 2 == 0:
        print(int((a + b) / 2))
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
    return

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    k = (a + b) / 2
    if k.is_integer():
        print(int(k))
    else:
        print('IMPOSSIBLE')

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    k = (a + b) // 2
    if abs(a - k) == abs(b - k):
        print(k)
    else:
        print('IMPOSSIBLE')

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    K = (A + B) / 2
    if K.is_integer():
        print(int(K))
    else:
        print("IMPOSSIBLE")

=======
Suggestion 7

def main():
    A, B = map(int, input().split())
    K = (A + B) // 2
    if (A + B) % 2 == 0:
        print(K)
    else:
        print("IMPOSSIBLE")

=======
Suggestion 8

def main():
    a,b = map(int, input().split())
    if (a + b) % 2 == 0:
        print((a + b) // 2)
    else:
        print('IMPOSSIBLE')
