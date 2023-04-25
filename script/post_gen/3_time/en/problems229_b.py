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
    if a + b < 10:
        print('Easy')
    else:
        print('Hard')

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a + b >= 10:
        print('Hard')
    else:
        print('Easy')

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a + b >= 10**10:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 5

def problems229_b():
    a, b = map(int, input().split())
    if a + b >= 10 ** 18:
        print('Hard')
    else:
        print('Easy')

=======
Suggestion 6

def main():
    a,b = map(int, input().split())
    if (a+b) >= 10**10:
        print('Hard')
    else:
        print('Easy')

=======
Suggestion 7

def solve(a, b):
    if a + b < 10:
        return "Easy"
    else:
        return "Hard"

=======
Suggestion 8

def solve(a, b):
    if a + b >= 10 ** 18:
        return "Hard"
    else:
        return "Easy"
