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
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

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
Suggestion 3

def main():
    A,B,C = map(int,input().split())
    if A==B and B==C:
        print("否")
    elif A==B or B==C or A==C:
        print("是")
    else:
        print("否")

=======
Suggestion 4

def main():
    a,b,c = map(int,input().split())
    if a == b and b == c:
        print("No")
    elif a == b or a == c or b == c:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    a,b,c = map(int,input().split())
    if a == b and b != c or a == c and a != b or b == c and a != b:
        print('是')
    else:
        print('否')

=======
Suggestion 6

def main():
    A, B, C = map(int, input().split())
    if A == B and A != C:
        print("是")
    elif B == C and B != A:
        print("是")
    elif A == C and A != B:
        print("是")
    else:
        print("否")
    return

=======
Suggestion 7

def check(x,y,z):
    if x==y and x!=z:
        return True
    elif x==z and x!=y:
        return True
    elif y==z and y!=x:
        return True
    else:
        return False

x,y,z=map(int,input().split())

=======
Suggestion 8

def main():
    a, b, c = map(int, input().split())
    if a == b and b != c:
        print('Yes')
    elif b == c and a != c:
        print('Yes')
    elif a == c and b != c:
        print('Yes')
    else:
        print('No')
