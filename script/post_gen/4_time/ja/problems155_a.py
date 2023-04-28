Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if a == b == c:
        print("No")
    elif a == b or b == c or c == a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    a,b,c = map(int,input().split())
    if a == b and b != c:
        print("Yes")
    elif b == c and c != a:
        print("Yes")
    elif c == a and a != b:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    A,B,C = map(int,input().split())
    if A == B and A != C:
        print("Yes")
    elif A == C and A != B:
        print("Yes")
    elif B == C and B != A:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

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
Suggestion 5

def main():
    a,b,c = map(int,input().split())
    if a == b == c:
        print('No')
    elif a == b or b == c or a == c:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def solve():
    a,b,c = map(int,input().split())
    if a == b == c:
        print('No')
    elif a == b or b == c or c == a:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def is_cute(A, B, C):
    if A == B and A != C:
        return True
    if B == C and B != A:
        return True
    if C == A and C != B:
        return True
    return False

A, B, C = map(int, input().split())

=======
Suggestion 8

def is_cute(a,b,c):
    if a==b and b!=c:
        return True
    elif a==c and c!=b:
        return True
    elif b==c and c!=a:
        return True
    else:
        return False

=======
Suggestion 9

def main():
    # 標準入力から値を取得する
    a, b, c = map(int, input().split())
    # a, b, cが全て等しいかどうか判定する
    if a == b and b == c:
        # 全て等しい場合はNoを出力する
        print('No')
    else:
        # 全て等しくない場合はYesを出力する
        print('Yes')
