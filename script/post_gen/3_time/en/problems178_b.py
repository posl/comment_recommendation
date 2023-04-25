Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c, d = map(int, input().split())
    print(max(a * c, a * d, b * c, b * d))

=======
Suggestion 2

def main():
    a, b, c, d = map(int, input().split())
    if a * d > b * c:
        print(a * d)
    else:
        print(b * c)

=======
Suggestion 3

def main():
    a, b, c, d = map(int, input().split())
    if a >= 0 or b <= 0:
        print(max(a * c, a * d, b * c, b * d))
    else:
        print(max(a * c, b * d))

=======
Suggestion 4

def main():
    a,b,c,d = map(int, input().split())
    max = a*c
    if a*d > max:
        max = a*d
    if b*c > max:
        max = b*c
    if b*d > max:
        max = b*d
    print(max)

=======
Suggestion 5

def main():
    a,b,c,d = map(int,input().split())
    if a*b < c*d:
        print(c*d)
    elif a*b > c*d:
        print(a*b)
    else:
        print(a*b)
