Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    print(max(a + b, b + c, c + a))

=======
Suggestion 2

def main():
    # input
    a, b, c = map(int, input().split())

    # compute

    # output
    print(max(a+b, b+c, c+a))

=======
Suggestion 3

def main():
    a,b,c = map(int, input().split())
    print(a+b+c-max(a,b,c))

=======
Suggestion 4

def main():
    A,B,C = map(int, input().split())
    print(A+B+C-max(A,B,C))

=======
Suggestion 5

def main():
    a,b,c = [int(i) for i in input().split()]
    print(a+b+c-max(a,b,c))

=======
Suggestion 6

def main():
    # input
    a,b,c = map(int, input().split())

    # output
    print(max(a+b, b+c, c+a))

=======
Suggestion 7

def main():
    a = input()
    a = a.split()
    a = [int(n) for n in a]
    a = sorted(a)
    print(a[1]+a[2])

=======
Suggestion 8

def solve():
    a,b,c = map(int,input().split())
    print(max(a+b,b+c,c+a))
    return 0

=======
Suggestion 9

def main():
    a = list(map(int, input().split()))
    print(max(a)*2)
