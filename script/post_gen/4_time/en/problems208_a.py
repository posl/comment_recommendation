Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a * 1 <= b <= a * 6:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a*6 >= b and a <= b:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if 6*a >= b and a <= b:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    if A <= B <= 6*A:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    if A <= B <= 6*A:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print('Yes' if a * 6 >= b and a <= b else 'No')

=======
Suggestion 7

def solve():
    a,b = map(int,input().split())
    if a*1 <= b <= a*6:
        print('Yes')
    else:
        print('No')
