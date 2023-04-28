Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, C, X = map(int, input().split())
    if X <= A:
        print(1.0)
    elif A < X <= B:
        print(C/(B-A))
    else:
        print(0.0)

=======
Suggestion 2

def main():
    A, B, C, X = map(int, input().split())
    if X <= A:
        print(1.0)
    elif A < X and X <= B:
        print(C/(B-A))
    else:
        print(0.0)

=======
Suggestion 3

def main():
    a,b,c,x = map(int, input().split())
    if x <= a:
        print(1.0)
    elif a < x <= b:
        print(c/(b-a))
    else:
        print(0.0)

=======
Suggestion 4

def main():
    a,b,c,x = map(int,input().split())
    if x <= a:
        print(1)
    elif a < x <= b:
        print(c/(b-a))
    else:
        print(0)

=======
Suggestion 5

def main():
    a, b, c, x = map(int, input().split())
    if x >= a:
        if x <= b:
            print(c / (b - a + 1))
        else:
            print(0)
    else:
        print(0)

=======
Suggestion 6

def main():
    A, B, C, X = map(int, input().split())
    if X <= A:
        print(1.0)
        return
    if A < X <= B:
        print(C / (B - A))
        return
    print(0.0)

=======
Suggestion 7

def main():
    A,B,C,X = map(int,input().split())
    if A >= X:
        print(0)
    elif A < X and X <= B:
        print((C)/(B-A))
    else:
        print(1)

=======
Suggestion 8

def main():
    a,b,c,x = map(int,input().split())
    if a <= x and x <= b:
        print(c/b)
    else:
        print(0)

=======
Suggestion 9

def calc_prob(A, B, C, X):
    if X <= A:
        return 1
    elif X <= B:
        return C / (B - A)
    else:
        return 0

=======
Suggestion 10

def main():
    # 入力値取得
    a, b, c, x = map(int, input().split())
    # 出力
    if x <= a:
        print(1)
    elif a < x <= b:
        print(c / (b - a))
    else:
        print(0)
