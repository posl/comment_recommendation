Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    print("输入三个数字，用空格分隔：")
    a,b,c = map(int,input().split())
    if a == b and a != c:
        print("Yes")
    elif a == c and a != b:
        print("Yes")
    elif b == c and a !

=======
Suggestion 2

def main():
    a,b,c = map(int,input().split())
    if a == b:
        if a != c:
            print("Yes")
        else:
            print("No")
    elif a == c:
        if a != b:
            print("Yes")
        else

=======
Suggestion 3

def main():
    a,b,c = map(int,input().split())
    if a==b and b!=c:
        print("Yes")
    elif a==c and b!=c:
        print("Yes")
    elif b==c and a!=c:
        print("Yes")
    else:

=======
Suggestion 4

def problem155a():
    a, b, c = map(int, input().split())
    if a == b and b != c:
        print("Yes")
    elif a == c and b != c:
        print("Yes")
    elif b == c and a != b:
        prin

=======
Suggestion 5

def main():
    A, B, C = map(int, input().split())
    if A == B and A != C:
        print('Yes')
    elif A == C and A != B:
        print('Yes')
    elif B == C and B != A:
        print('Yes'

=======
Suggestion 6

def main():
    a,b,c = map(int,input().split())
    if a==b and b!=c:
        print("Yes")
    elif a==c and b!=c:
        print("Yes")
    elif b==c and a!=b:
        print("Yes")
    else:

=======
Suggestion 7

def main():
    A,B,C = map(int, input().split())
    if A == B and A != C:
        print("Yes")
    elif A == C and A != B:
        print("Yes")
    elif B == C and B != A:
        print("Yes")

=======
Suggestion 8

def main():
    a,b,c = map(int,input().split())
    if a == b and a != c:
        print("Yes")
    elif a == c and a != b:
        print("Yes")
    elif b == c and b != a:
        print("Yes")

=======
Suggestion 9

def is_diff(a, b, c):
    if a == b and b != c:
        return True
    elif b == c and c != a:
        return True
    elif c == a and a != b:
        return True
    else:
        return False

=======
Suggestion 10

def main():
    A, B, C = map(int, input().split())
    if A == B and B != C:
        print("Yes")
    elif A == C and B != C:
        print("Yes")
    elif B == C and A != B:
        print("Yes"
