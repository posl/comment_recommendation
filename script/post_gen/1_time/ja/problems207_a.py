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
    print(max(a+b, b+c, c+a))

=======
Suggestion 3

def main():
    a,b,c = map(int,input().split())
    print(a+b+c-max(a,b,c))

=======
Suggestion 4

def main():
    abc = list(map(int, input().split()))
    abc.sort()
    print(abc[1] + abc[2])

=======
Suggestion 5

def solve():
    a,b,c = map(int, input().split())
    print(a+b+c-max(a,b,c))

=======
Suggestion 6

def main():
    a,b,c = list(map(int, input().rstrip().split()))
    print(a+b+c)
