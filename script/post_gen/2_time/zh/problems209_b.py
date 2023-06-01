Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print(b - a + 1 if b > a else 0)

=======
Suggestion 2

def main():
    A,B = map(int,input().split())
    if A > B:
        print(0)
    else:
        print(B-A+1)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    count = 0
    for i in range(a, b + 1):
        count += 1
    print(count)

=======
Suggestion 4

def func():
    a,b = map(int,input().split())
    if a > b:
        print(0)
    else:
        print(b-a+1)

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    print(b - a + 1 if b - a >= 0 else 0)

=======
Suggestion 6

def count_integer(a,b):
    if a <= b and a >= 1 and b <= 100:
        return b - a + 1
    else:
        return 0

=======
Suggestion 7

def main():
    A, B = map(int, input().split())
    print(B-A+1 if B-A>=0 else 0)

=======
Suggestion 8

def main():
    a,b = map(int,input().split())
    if a > b:
        print(0)
    else:
        print(b-a+1)

=======
Suggestion 9

def main():
    a,b = map(int,input().split())
    print(b-a+1 if b-a+1 > 0 else 0)
