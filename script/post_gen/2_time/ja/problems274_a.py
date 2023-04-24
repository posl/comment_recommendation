Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print('{:.3f}'.format(b/a))

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    print("{:.3f}".format(b/a))

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    C = B / A
    D = round(C, 3)
    print('{:.3f}'.format(D))

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    print("{0:.3f}".format(b/a))

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    print("{:.3f}".format((b/a)))

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    print('{:.3f}'.format(B / A))

=======
Suggestion 7

def main():
    a, b = list(map(int, input().strip().split()))
    print('{:.3f}'.format(round(b/a, 4)))

=======
Suggestion 8

def main():
    a,b = map(int, input().split())
    print("{:0.3f}".format(b/a))

=======
Suggestion 9

def main():
    a, b = map(int, input().split())
    print("{:03}".format(round(b/a, 3)*1000))

=======
Suggestion 10

def calc():
    a,b = map(int, input().split())
    print("{:.3f}".format(b/a))
