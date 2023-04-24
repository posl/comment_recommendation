Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = int(input())
    if x == 0:
        print("No")
    elif x % 100 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    x = int(input())
    if x % 100 == 0 and x != 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    x = int(input())
    if x % 100 == 0 and x != 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    X = int(input())
    if X % 100 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def solve():
    x = int(input())
    if x % 100 == 0 and x != 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    x = int(input())
    if x % 100 == 0 and x >= 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def check(x):
    if x%100 == 0:
        return True
    else:
        return False

=======
Suggestion 8

def solve(X):
    return "Yes" if X%100 == 0 else "No"
