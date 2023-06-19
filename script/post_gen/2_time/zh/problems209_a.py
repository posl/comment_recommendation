Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b=map(int,input().split())
    if a>b:
        print(0)
    else:
        print(b-a+1)

=======
Suggestion 2

def main():
    a,b = map(int,input().split())
    print(b-a+1 if b-a>=0 else 0)

=======
Suggestion 3

def problems209_a():
    a, b = map(int, input().split())
    print(b - a + 1 if b >= a else 0)

=======
Suggestion 4

def main():
    a,b = map(int, input().split())
    print(b-a+1 if b-a>0 else 0)

=======
Suggestion 5

def count_num(a,b):
    count = 0
    for i in range(a,b+1):
        count += 1
    return count

a, b = map(int, input().split())
print(count_num(a,b))

=======
Suggestion 6

def main():
    a,b = map(int, input().split())
    print(b - a + 1 if b >= a else 0)

=======
Suggestion 7

def main():
    A,B = map(int,input().split())
    print(B-A+1 if B-A >= 0 else 0)

=======
Suggestion 8

def problem209_a():
    a, b = map(int, input().split())
    print(b - a + 1 if a <= b else 0)
