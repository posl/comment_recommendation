Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if b - a == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if b - a == 1 or b - a == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if b - a == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a + 1 == b:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def is_connected(a, b):
    if a == 1 and b == 2:
        return True
    if a == 1 and b == 3:
        return True
    if a == 1 and b == 4:
        return True
    if a == 1 and b == 5:
        return True
    if a == 2 and b == 3:
        return True
    if a == 2 and b == 4:
        return True
    if a == 2 and b == 5:
        return True
    if a == 2 and b == 6:
        return True
    if a == 3 and b == 4:
        return True
    if a == 3 and b == 5:
        return True
    if a == 3 and b == 6:
        return True
    if a == 3 and b == 7:
        return True
    if a == 4 and b == 5:
        return True
    if a == 4 and b == 6:
        return True
    if a == 4 and b == 7:
        return True
    if a == 4 and b == 8:
        return True
    if a == 5 and b == 6:
        return True
    if a == 5 and b == 7:
        return True
    if a == 5 and b == 8:
        return True
    if a == 5 and b == 9:
        return True
    if a == 6 and b == 7:
        return True
    if a == 6 and b == 8:
        return True
    if a == 6 and b == 9:
        return True
    if a == 6 and b == 10:
        return True
    if a == 7 and b == 8:
        return True
    if a == 7 and b == 9:
        return True
    if a == 7 and b == 10:
        return True
    if a == 8 and b == 9:
        return True
    if a == 8 and b == 10:
        return True
    if a == 9 and b == 10:
        return True
    return False

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    if (a + 1) == b:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def problems240_a():
    a, b = map(int, input().split())
    if a+1 == b:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def check(a,b):
    if (a < b) and (1 <= a) and (b <= 10):
        return True
    else:
        return False

a,b = map(int, input().split())
