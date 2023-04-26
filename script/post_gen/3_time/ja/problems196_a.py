Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(b - c, d - a))

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(b-d, b-c, a-d, a-c))

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(a - d, b - c))

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(a-c, a-d, b-c, b-d))

=======
Suggestion 5

def main():
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    print(max(abs(a-c),abs(a-d),abs(b-c),abs(b-d)))
