Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print("{0:0.3f}".format(b/a))

=======
Suggestion 2

def main():
    A,B = map(int,input().split())
    print("{:.3f}".format(round(B/A,3)))

=======
Suggestion 3

def main():
    A,B = map(int, input().split())
    ans = B/A
    ans = round(ans,4)
    print('{:.3f}'.format(ans))
    return

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    print("{0:.3f}".format(b/a))

=======
Suggestion 5

def main():
    A,B = map(int,input().split())
    print("{:.3f}".format(B/A))

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print('{:.3f}'.format(b/a))

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    print("{:.3f}".format(b/a))

=======
Suggestion 8

def func(a,b):
    return round(b/a,4)

a,b = map(int,input().split())
print('{:.3f}'.format(func(a,b)))
