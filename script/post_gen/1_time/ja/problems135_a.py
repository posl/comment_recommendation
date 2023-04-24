Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if (a + b) % 2 == 0:
        print((a + b) // 2)
    else:
        print("IMPOSSIBLE")

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
    k = (a + b) / 2
    if k.is_integer():
        print(int(k))
    else:
        print("IMPOSSIBLE")

=======
Suggestion 4

def main():
    a, b = map(int, input().split())

    if (a+b)%2 == 0:
        print(int((a+b)/2))
    else:
        print('IMPOSSIBLE')

=======
Suggestion 5

def main():
    a,b = map(int, input().split())
    if a > b:
        print(a - (a - b) // 2)
    else:
        print(b - (b - a) // 2)

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    if a>b:
        tmp = a
        a = b
        b = tmp
    if (a+b)%2 == 0:
        print(int((a+b)/2))
    else:
        print("IMPOSSIBLE")

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    if(a > b):
        print(a - (a - b) // 2)
    else:
        print(b - (b - a) // 2)

=======
Suggestion 8

def main():
    A,B = map(int, input().split())
    if A > B:
        K = (A + B) // 2
        if abs(A - K) == abs(B - K):
            print(K)
        else:
            print("IMPOSSIBLE")
    else:
        K = (A + B) // 2
        if abs(A - K) == abs(B - K):
            print(K)
        else:
            print("IMPOSSIBLE")
