Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(b - c)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(a - c, a - d, b - c, b - d))

=======
Suggestion 3

def main():
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    print(b-d)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(b-c, b-d, a-c, a-d))

=======
Suggestion 5

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(max(a-c,a-d,b-c,b-d))

=======
Suggestion 6

def max(x,y):
    if x > y:
        return x
    else:
        return y
