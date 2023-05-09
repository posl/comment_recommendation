Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a + b < 10:
        print("Easy")
    else:
        print("Hard")

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if (a + b) < 10:
        print('Easy')
    else:
        print('Hard')

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if (a + b) % 2 == 0:
        print('Easy')
    else:
        print('Hard')

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a + b >= 10:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    sum = a + b
    if sum < 10:
        print("Easy")
    else:
        print("Hard")

=======
Suggestion 6

def solve():
    a, b = map(int, input().split())
    if a + b < 10:
        print("Easy")
    else:
        print("Hard")

=======
Suggestion 7

def solve(a,b):
    if a+b < 10:
        return 'Easy'
    else:
        return 'Hard'
