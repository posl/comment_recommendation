Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A,B = map(int, input().split()

=======
Suggestion 2

def main():
    a,b = map(int, input().split())
    x = a / pow(a*a+b*b, 0.5)
    y = b / pow(a*a+b*b, 0.5)
    print(x, y)

main()

=======
Suggestion 3

def main():
    a,b = map(int, input().split())
    tmp = b/a
    #print(tmp)
    if a > b:
        tmp2 = (1-tmp**2)**0.5
        print(tmp2)
        print(1-tmp**2)
        print(tmp2)
        print(tmp)
    else:
        tmp2 = (1-tmp**2)**0.5
        print(tmp2)
        print(1-tmp**2)
        print(tmp2)
        print(tmp)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    #print(a, b)
    #print(a / (a + b), b / (a + b))
    print("{:.12f} {:.12f}".format(a / (a + b), b / (a + b)))

=======
Suggestion 5

def main():
    a,b = map(int,input().split())
    x = a/(a**2 + b**2)**0.5
    y = b/(a**2 + b**2)**0.5
    print(x,y)

=======
Suggestion 6

def solve():
    A,B = map(int,input().split())
    print(B/A)

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    c = (a**2+b**2)**0.5
    x = a/c
    y = b/c
    print(x,y)

=======
Suggestion 8

def solve():
    a, b = map(int, input().split())
    if a == 0:
        print(0, 1)
    elif b == 0:
        print(1, 0)
    else:
        c = (b**2 / a**2 + 1) ** 0.5
        print(1 / (1 + c), c / (1 + c))

=======
Suggestion 9

def main():
    a, b = map(int, input().split())
    if a == 0:
        print(0, 1)
        return
    if b == 0:
        print(1, 0)
        return
    if a == b:
        print(0.5, 0.5)
        return
    if a > b:
        print((a - b) / (2 * a), 0.5 + (a - b) / (2 * b))
        return
    if b > a:
        print(0.5 + (b - a) / (2 * a), (b - a) / (2 * b))
        return

=======
Suggestion 10

def main():
    A, B = map(int, input().split())
    print(A / (A + B), B / (A + B))
