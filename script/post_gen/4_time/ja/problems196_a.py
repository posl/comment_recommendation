Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(a-c, a-d, b-c, b-d))

=======
Suggestion 2

def solve():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(a - c, a - d, b - c, b - d))

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(max(a, c) - min(b, d), 0))

=======
Suggestion 4

def main():
    a,b = map(int, input().split())
    c,d = map(int, input().split())
    print(b-d)
