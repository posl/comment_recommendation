Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if (a + b) % 2 == 0:
        print((a + b) // 2)
    else:
        print("IMPOSIBLE")

=======
Suggestion 2

def solve():
    A, B = map(int, input().split())
    if (A + B) % 2 == 0:
        print((A + B) // 2)
    else:
        print('IMPOSSIBLE')

=======
Suggestion 3

def calc_k(a,b):
    if a == b:
        return "IMPOSSIBLE"
    else:
        return (a+b)//2

=======
Suggestion 4

def solve():
    a, b = map(int, input().split())
    if (a+b)%2 == 0:
        print((a+b)//2)
    else:
        print('IMPOSIBLE')

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    if (A+B)%2 == 0:
        print((A+B)//2)
    else:
        print("IMPOSIBLE")

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    if a==b:
        print(a)
    elif a>b:
        print(a)
    else:
        print(b)

=======
Suggestion 7

def solution(a, b):
    if a == b:
        return "IMPOSIBLE"
    if a > b:
        if (a - b) % 2 == 0:
            return int((a - b) / 2 + b)
        else:
            return "IMPOSIBLE"
    else:
        if (b - a) % 2 == 0:
            return int((b - a) / 2 + a)
        else:
            return "IMPOSIBLE"

=======
Suggestion 8

def main():
    A, B = map(int, input().split())
    if (A + B) % 2 == 0:
        print((A + B) // 2)
    else:
        print("IMPOSSIBLE")

=======
Suggestion 9

def problems135_a():
    a,b = map(int,input().split())
    if a >= b:
        if (a-b)%2 == 0:
            print((a-b)//2 + b)
        else:
            print("IMPOSSIBLE")
    else:
        if (b-a)%2 == 0:
            print((b-a)//2 + a)
        else:
            print("IMPOSSIBLE")

=======
Suggestion 10

def main():
    A, B = map(int, input().split())
    if (A+B) % 2 != 0:
        print("IMPOSSIBLE")
    else:
        print((A+B)//2)
