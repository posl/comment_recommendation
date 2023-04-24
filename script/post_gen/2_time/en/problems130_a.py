Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, a = map(int, input().split())
    if x < a:
        print(0)
    else:
        print(10)

=======
Suggestion 2

def main():
    X, A = map(int, input().split())
    if X < A:
        print(0)
    else:
        print(10)

=======
Suggestion 3

def main():
    X, A = input().split()
    if int(X) < int(A):
        print(0)
    else:
        print(10)

=======
Suggestion 4

def main():
    x, a = [int(x) for x in input().split()]
    if x < a:
        print(0)
    else:
        print(10)

=======
Suggestion 5

def main():
    X, A = input().split()
    if int(X) < int(A):
        print('0')
    else:
        print('10')

=======
Suggestion 6

def main():
    # read input
    x, a = map(int, input().split())

    # output
    if x < a:
        print(0)
    else:
        print(10)
