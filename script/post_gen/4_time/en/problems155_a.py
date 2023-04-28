Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if a == b and b != c:
        print("Yes")
    elif b == c and c != a:
        print("Yes")
    elif c == a and a != b:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def is_poor(a, b, c):
    if a == b and b != c:
        return True
    elif a == c and b != c:
        return True
    elif b == c and a != c:
        return True
    else:
        return False

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if a == b and b != c:
        print("Yes")
    elif b == c and c != a:
        print("Yes")
    elif a == c and c != b:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    a,b,c = map(int, input().split())
    if a==b and b!=c:
        print("Yes")
    elif b==c and c!=a:
        print("Yes")
    elif c==a and a!=b:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 5

def main():
    A, B, C = input().split()
    if A == B and A != C:
        print("Yes")
    elif A == C and A != B:
        print("Yes")
    elif B == C and B != A:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

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
Suggestion 7

def main():
    a, b, c = map(int, input().split())
    if a == b and a == c:
        print("No")
    elif a == b or b == c or a == c:
        print("Yes")
    else:
        print("No")
main()

=======
Suggestion 8

def poor_triple(a, b, c):
    if a == b and b != c:
        return True
    if b == c and c != a:
        return True
    if c == a and a != b:
        return True
    return False
