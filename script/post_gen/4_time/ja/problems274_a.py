Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print("{:.3f}".format(b/a))

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    print("{:.3f}".format(round(b/a, 4)))

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    print('{:.3f}'.format(B/A))

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    print('{:.3f}'.format(b/a))

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    print('{0:0.3f}'.format(round(B/A, 3)))

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    print(str(round(B/A, 4))[:5])
