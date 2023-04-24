Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print('{:.3f}'.format(b/a))

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    print("{:.3f}".format(B/A))

=======
Suggestion 3

def main():
    A, B = [int(i) for i in input().split()]
    print("{:.3f}".format(B/A))

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    print("%.3f" % (b / a))

=======
Suggestion 5

def main():
    A,B = [int(x) for x in input().split()]
    print("{0:.3f}".format(B/A))

=======
Suggestion 6

def main():
    a,b = map(int, input().split())
    print('{:.3f}'.format(b/a))
main()

=======
Suggestion 7

def main():
    A, B = input().split()
    print(str(round(int(B) / int(A), 3)))
