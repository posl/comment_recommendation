Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c = map(int, input().split())
    if a == b and b == c:
        print('No')
    elif a == b or b == c or c == a:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

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
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if a == b and b != c:
        print("Yes")
    elif a == c and b != c:
        print("Yes")
    elif b == c and a != c:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def solve():
    # 解答をここに書く
    A, B, C = map(int, input().split())
    if A == B:
        if A != C:
            print("Yes")
        else:
            print("No")
    elif A == C:
        if A != B:
            print("Yes")
        else:
            print("No")
    elif B == C:
        if A != B:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    if a == b == c:
        print('No')
    elif a == b or b == c or c == a:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def solve():
    a, b, c = map(int, input().split())
    if a == b and b != c:
        print('Yes')
    elif b == c and c != a:
        print('Yes')
    elif c == a and a != b:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    a,b,c = map(int,input().split())
    if a == b:
        if a == c:
            print("No")
        else:
            print("Yes")
    elif b == c:
        print("Yes")
    elif a == c:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    a, b, c = map(int, input().split())
    if a == b and a != c:
        print('Yes')
    elif a == c and a != b:
        print('Yes')
    elif b == c and b != a:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    a,b,c = map(int, input().split())
    if a == b == c:
        print('No')
    elif a == b or b == c or a == c:
        print('Yes')
    else:
        print('No')
