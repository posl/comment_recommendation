Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    print(a + b + c - min(a, b, c))

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if a == b and b == c:
        print(a * 3)
    else:
        print(max(a, b, c) * 2)

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    print(max(a+b, b+c, c+a))

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    print(max(a+b, a+c, b+c))

=======
Suggestion 5

def main():
    a,b,c = map(int,input().split())
    print(a+b+c-max(a,b,c))

=======
Suggestion 6

def main():
    A,B,C = map(int,input().split())
    print(A+B+C-max(A,B,C))
