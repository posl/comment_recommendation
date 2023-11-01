Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读取输入
    a, b, c = map(int, input().split())

    # 判断
    if a == b and b != c:
        print("Yes")
    elif a == c and b != c:
        print("Yes")
    elif b

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if a == b:
        if a != c:
            print("Yes")
        else:
            print("No")
    elif a == c:
        if a != b:

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if a == b == c:
        print('No')
    elif a == b or b == c or c == a:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    A,B,C = map(int,input().split())
    if A == B and B == C:
        print("No")
    elif A == B or B == C or A == C:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def f(a, b, c):
    if a == b and b != c:
        return True
    elif a == c and c != b:
        return True
    elif b == c and c != a:
        return True
    else:
        return False

=======
Suggestion 6

def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 判断
    if a == b and a != c:
        print("Yes")
    elif a == c and a != b:
        print("Yes")
    elif b =

=======
Suggestion 7

def main():
    a,b,c = map(int,input().split())
    if a == b and a != c:
        print("Yes")
    elif a == c and a != b:
        print("Yes")
    elif b == c and b != a:

=======
Suggestion 8

def main():
    a,b,c = map(int, input().split())
    if a == b and b == c:
        print("No")
    elif a == b:
        print("Yes")
    elif b == c:
        print("Yes")
    elif

=======
Suggestion 9

def main():
    a,b,c = map(int,input().split())
    if a==b and a!=c:
        print("Yes")
    elif a==c and a!=b:
        print("Yes")
    elif b==c and b!=a:
        print("Yes"

=======
Suggestion 10

def solve():
    a,b,c = map(int, input().split())
    if a==b and b!=c:
        print("Yes")
    elif a==c and c!=b:
        print("Yes")
    elif b==c and c!=a:
        print("Ye
