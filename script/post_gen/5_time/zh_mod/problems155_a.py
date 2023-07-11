Synthesizing 10/10 solutions

=======
Suggestion 1

def is_diff(a, b, c):
    if a == b and b != c:
        return True
    elif a == c and c != b:
        return True
    elif b == c and c != a:
        return True
    else:

=======
Suggestion 2

def main():
    a,b,c = map(int, input().split())
    if a == b and a != c:
        print("Yes")
    elif a == c and a != b:
        print("Yes")
    elif b == c and b != a:

=======
Suggestion 3

def IsDiff(a,b,c):
    if a == b and a != c:
        return True
    elif a == c and a != b:
        return True
    elif b == c and b != a:
        return True
    else:
        return False

=======
Suggestion 4

def check():
    a,b,c=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    if a==b and b!=c:
        print("Yes")
    elif a==c and b!=c:
        print("Yes")
    elif b=

=======
Suggestion 5

def main():
    # 读取输入
    A, B, C = map(int, input().split())

    # 决定输出
    if A == B and B != C:
        print("Yes")
    elif A == C and A != B:
        print("Yes")
    el

=======
Suggestion 6

def main():
    a,b,c = map(int,input().split())
    if a==b and b!=c:
        print("Yes")
    elif a==c and a!=b:
        print("Yes")
    elif b==c and b!=a:
        print("Y

=======
Suggestion 7

def main():
    A, B, C = map(int, input().split())
    if (A == B and A != C) or (A == C and A != B) or (B == C and B != A):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def check(a,b,c):
    if a==b and a!=c:
        return True
    elif a==c and a!=b:
        return True
    elif b==c and b!=a:
        return True
    else:
        return False

=======
Suggestion 9

def main():
    a,b,c = map(int, input().split())
    if a == b and b == c:
        print("No")
    elif a == b or b == c or a == c:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    A,B,C = map(int,input().split())
    if A == B and A != C:
        print('Yes')
    elif A == C and A != B:
        print('Yes')
    elif B == C and B != A:
