Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    c, d = map(int, input

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(b - c, d - a))

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(b-d, b-c, a-d, a-c))

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(b - c, a - d))

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    if a <= c <= b:
        print(max(b - c, d - a))
    elif c <= a <= d:
        print(max(b - c, d - a))
    else:
        print(max(b - a, d - c))
