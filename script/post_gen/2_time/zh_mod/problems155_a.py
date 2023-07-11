Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c = map(int,input().split())
    if a == b and b != c:
        print("Yes")
    elif a == c and b != c:
        print("Yes")
    elif b == c and a != c:
        print(

=======
Suggestion 2

def main():
    a,b,c=map(int,input().split())
    if a==b and a!=c:
        print("Yes")
    elif a==c and a!=b:
        print("Yes")
    elif b==c and b!=a:
        print("Yes")
    els

=======
Suggestion 3

def main():
    a,b,c = map(int, input().split())
    if a == b and a != c:
        print("Yes")
    elif a == c and a != b:
        print("Yes")
    elif b == c and b != a:
        print

=======
Suggestion 4

def main():
    a,b,c = map(int,input().split())
    if a==b and b!=c:
        print("Yes")
    elif a==c and b!=c:
        print("Yes")
    elif b==c and a!=c:
        print("Yes")
    e

=======
Suggestion 5

def main():
    A,B,C = map(int,input().split())
    if A == B and A != C:
        print("Yes")
    elif A == C and A != B:
        print("Yes")
    elif B == C and B != A:
        print(

=======
Suggestion 6

def main():
    a, b, c = map(int, input().split())
    if a == b and b == c:
        print("No")
    elif a == b or a == c or b == c:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    a, b, c = map(int, input().split())
    if a == b and b != c:
        print('Yes')
    elif a == c and b != c:
        print('Yes')
    elif b == c and a != b:

=======
Suggestion 8

def main():

    # 读取输入
    a, b, c = map(int, input().split())

    # 逻辑处理
    if a == b and b != c:
        print('Yes')
    elif a == c and b != c:
        print('Yes')
    elif b == c and a != b:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    a,b,c = map(int,input().split())
    if a == b and b == c:
        print('No')
    elif a == b or b == c or c == a:
        print('Yes')
    else:
        print('No')
