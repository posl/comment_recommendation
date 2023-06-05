Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a == b:
        print(a+b)
    elif a > b:
        print(a+a-1)
    else:
        print(b+b-1)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    print(max(A + A - 1, A + B, B + B - 1))

=======
Suggestion 3

def main():
    # 读取输入
    A, B = map(int, input().split())
    # 计算结果
    if A == B:
        print(A + B)
    elif A > B:
        print(A + A - 1)
    else:
        print(B + B - 1)

=======
Suggestion 4

def main():
    a,b = map(int, input().split())
    print(max(a+b, a+b-1, a*2-1, b*2-1))

=======
Suggestion 5

def max_coin(a, b):
    if a < b:
        return b + b - 1
    elif a > b:
        return a + a - 1
    else:
        return a + b

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    if A == B:
        print(A*2)
    else:
        print(max(A, B)*2-1)

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    if a > b:
        print(a+(a-1))
    elif a < b:
        print(b+(b-1))
    else:
        print(a+b)

=======
Suggestion 8

def main():
    a,b = map(int, input().split())
    if a > b:
        print(a+a-1)
    elif a < b:
        print(b+b-1)
    else:
        print(a+b)

=======
Suggestion 9

def get_coins(A, B):
    if A >= B:
        return A + (A-1)
    else:
        return B + (B-1)

=======
Suggestion 10

def main():
    A,B = map(int,input().split())
    if A == B:
        print(A*2)
    elif A > B:
        print(A+A-1)
    else:
        print(B+B-1)
