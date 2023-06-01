Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b,c = map(int,input().split())
    if a == b and b != c:
        print("Yes")
    elif a == c and b != c:
        print("Yes")
    elif b == c and a != c:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    a,b,c=map(int,input().split())
    if a==b and b!=c:
        print("是")
    elif b==c and c!=a:
        print("是")
    elif c==a and a!=b:
        print("是")
    else:
        print("否")

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if a == b and a != c:
        print("Yes")
    elif a == c and a != b:
        print("Yes")
    elif b == c and b != a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def answer(A,B,C):
    if A == B and B != C:
        return "是"
    elif A == C and B != C:
        return "是"
    elif B == C and A != B:
        return "是"
    else:
        return "否"

=======
Suggestion 5

def is_diff(a, b, c):
    if a == b and a != c:
        return True
    elif a == c and a != b:
        return True
    elif b == c and b != a:
        return True
    else:
        return False

=======
Suggestion 6

def problem155_a():
    a,b,c = map(int,input().split())
    if a==b and b!=c:
        print('是')
    elif a==c and b!=c:
        print('是')
    elif b==c and a!=b:
        print('是')
    else:
        print('否')

=======
Suggestion 7

def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 判断
    if a == b:
        if a == c:
            print("否")
        else:
            print("是")
    elif b == c:
        print("是")
    elif a == c:
        print("是")
    else:
        print("否")

=======
Suggestion 8

def main():
    a,b,c = map(int,input().split())
    if a==b and a!=c:
        print("是")
    elif a==c and a!=b:
        print("是")
    elif b==c and b!=a:
        print("是")
    else:
        print("否")

=======
Suggestion 9

def problem155_a():
    a,b,c = map(int,input().split())
    if a == b and a != c:
        print("Yes")
    elif a == c and a != b:
        print("Yes")
    elif b == c and b != a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    a, b, c = map(int, input().split())
    if a == b and b != c:
        print("是")
    elif b == c and a != c:
        print("是")
    elif a == c and b != c:
        print("是")
    else:
        print("否")
