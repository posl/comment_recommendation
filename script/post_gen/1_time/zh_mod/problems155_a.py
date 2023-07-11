Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if a == b:
        if a != c:
            print("Yes")
        else:
            print("No")
    elif a == c:
        if a != b:
            print("Yes")

=======
Suggestion 2

def main():
    a,b,c=map(int,input().split())
    if a==b and b!=c:
        print("Yes")
    elif a==c and b!=c:
        print("Yes")
    elif b==c and a!=c:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    A, B, C = map(int, input().split())
    if A == B and B == C:
        print("No")
    elif A == B or B == C or A == C:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    if A == B and A != C:
        print("Yes")
    elif B == C and B != A:
        print("Yes")
    elif A == C and A != B:
        print("Yes")
    els

=======
Suggestion 5

def problems155_a():
    a,b,c = input().split()
    if a==b and a!=c:
        print('Yes')
    elif a==c and a!=b:
        print('Yes')
    elif b==c and b!=a:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    a, b, c = map(int, input().split())
    if a == b and b == c:
        print("No")
    elif a == b and b != c:
        print("Yes")
    elif b == c and c != a:
        print("Yes")
    elif

=======
Suggestion 7

def main():
    a,b,c = map(int, input().split())
    if a == b and b != c:
        print('Yes')
    elif b == c and c != a:
        print('Yes')
    elif c == a and a != b:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    a,b,c=map(int,input().split())
    if a==b and a!=c:
        print("Yes")
    elif a==c and a!=b:
        print("Yes")
    elif b==c and b!=a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def is_triple_double(a, b, c):
    if a == b and a != c:
        return True
    elif a == c and a != b:
        return True
    elif b == c and b != a:
        return True
    else:
        return False
