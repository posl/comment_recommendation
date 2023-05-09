Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def is_poor(a, b, c):
    if a == b and a != c:
        return True
    elif a == c and a != b:
        return True
    elif b == c and b != a:
        return True
    else:
        return False

a, b, c = map(int, input().split())
print("Yes" if is_poor(a, b, c) else "No")

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if a == b and a != c:
        print("Yes")
    elif b == c and b != a:
        print("Yes")
    elif c == a and c != b:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def is_poor(a, b, c):
    if a == b and a != c:
        return True
    if a == c and a != b:
        return True
    if b == c and a != b:
        return True
    return False

=======
Suggestion 4

def main():
    a,b,c = map(int, input().split())
    if a == b and b == c:
        print("No")
    elif a == b or b == c or c == a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    a, b, c = list(map(int, input().split()))
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
    a,b,c = map(int, input().split())
    if (a == b and b != c) or (b == c and a != c) or (a == c and a != b):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def problem155_a():
    a, b, c = map(int, input().split())
    if a == b and b != c:
        print('Yes')
    elif a == c and c != b:
        print('Yes')
    elif b == c and c != a:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    x = list(map(int, input().split()))
    if x[0] == x[1] and x[1] == x[2]:
        print('No')
    elif x[0] == x[1] or x[1] == x[2] or x[2] == x[0]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    # Get input here
    A, B, C = map(int, input().strip().split())
    # Calculate result here
    if A == B and B == C:
        print("No")
    elif A == B or B == C or A == C:
        print("Yes")
    else:
        print("No")

main()
