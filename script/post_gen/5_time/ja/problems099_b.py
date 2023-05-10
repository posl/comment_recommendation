Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print((b-a)*(b-a+1)//2-b)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    print(b - a - 1 - sum(range(a + 1)))

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print((b-a)*(b-a-1)//2-a)

=======
Suggestion 4

def solve():
    a, b = map(int, input().split())
    print(b - a - 1 - sum(range(1, b - a)))

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    print(b-a-1)

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print(sum(range(1, b - a)) - a)

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    print(int((b-a)*(b-a+1)/2 - b))

=======
Suggestion 8

def solve():
    a,b = map(int,input().split())
    print(b-a-1)
