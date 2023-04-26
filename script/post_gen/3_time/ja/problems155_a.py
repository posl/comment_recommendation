Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    A, B, C = map(int, input().split())
    if A == B and A != C:
        print("Yes")
    elif A == C and A != B:
        print("Yes")
    elif B == C and B != A:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if a == b == c:
        print("No")
    elif a == b or b == c or a == c:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

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
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    if a == b and b != c:
        print('Yes')
    elif a == c and b != c:
        print('Yes')
    elif b == c and a != c:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    a,b,c = map(int,input().split())
    if a == b and b != c:
        print('Yes')
    elif b == c and c != a:
        print('Yes')
    elif c == a and a != b:
        print('Yes')
    else:
        print('No')
