Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def max(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a,b = map(int,input().split())
print(max(a+b,a-b,a*b))

=======
Suggestion 2

def main():
    a,b = map(int, input().split())
    print(max(a+b, a-b, a*b))

=======
Suggestion 3

def max(a,b):
    if a > b:
        return a
    else:
        return b

=======
Suggestion 4

def func(a, b):
    print(max(a+b, a-b, a*b))
