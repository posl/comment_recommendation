Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    print(min(B//A, C))

=======
Suggestion 2

def problems120_a():
    a,b,c = map(int,input().split())
    print(min(b//a,c))

=======
Suggestion 3

def main():
    A,B,C = map(int,input().split())
    if A * C <= B:
        print(C)
    else:
        print(B // A)

=======
Suggestion 4

def problems120_a():
    print("问题120：")
    a,b,c = map(int,input().split())
    print(min(b//a,c))
    print("问题120完成！")

=======
Suggestion 5

def main():
    a,b,c = map(int, input().split())
    if a*c <= b:
        print(c)
    else:
        print(b//a)

=======
Suggestion 6

def main():
    a,b,c=map(int,input().split())
    if a*c>=b:
        print(b//a)
    else:
        print(c)

=======
Suggestion 7

def problem120_a():
    A,B,C = map(int,input().split())
    if A*C <= B:
        print(C)
    else:
        print(B//A)

=======
Suggestion 8

def max_count(a,b,c):
    count = 0
    if c > b // a:
        count = b // a
    else:
        count = c
    return count

=======
Suggestion 9

def main():
    a, b, c = map(int, input().split())
    if b // a > c:
        print(c)
    else:
        print(b // a)
