Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, c, x = map(int, input().split())
    if x <= a:
        print(1)
    elif a < x <= a + c:
        print(1 / (b - a + 1))
    else:
        print(0)

=======
Suggestion 2

def main():
    A, B, C, X = map(int, input().split())
    if X <= A:
        print(1)
    elif A < X <= A+C:
        print((C+1)/(B-A+1))
    else:
        print(0)

=======
Suggestion 3

def main():
    # 入力
    A, B, C, X = map(int, input().split())
    # 出力
    if X <= A:
        print(1)
    elif X <= B:
        print(C / (B - A + 1))
    else:
        print(0)

=======
Suggestion 4

def main():
    A, B, C, X = map(int, input().split())
    print(1 - (B - X) / (B - A) * (B - A - C) / (B - A))

=======
Suggestion 5

def main():
    a,b,c,x=map(int,input().split())
    if x<=a:
        print(1)
    elif a<x<=a+c:
        print((c+1)/(b-a+1))
    else:
        print(0)

=======
Suggestion 6

def main():
    A, B, C, X = map(int, input().split())
    print(1 - (B - X) / (B - A) * (C - 1) / C)

=======
Suggestion 7

def main():
    A,B,C,X = [int(x) for x in input().split()]
    if X <= A:
        print(1)
    elif A < X <= A+C:
        print((C+1)/(B-A+1))
    else:
        print(0)

=======
Suggestion 8

def main():
    A,B,C,X = map(int,input().split())
    if X <= A:
        print(1)
    elif X <= B:
        print((B-X+1)/B)
    else:
        print(0)

=======
Suggestion 9

def main():
    A,B,C,X = map(int,input().split())
    if A<=X<=B:
        print((C/(B-A+1)))
    else:
        print(0)

=======
Suggestion 10

def main():
    A,B,C,X = map(int,input().split())
    print((C/B)*((B-C)/(B-A))**(X-A-1))
