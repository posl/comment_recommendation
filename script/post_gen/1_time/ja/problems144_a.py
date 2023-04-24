Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a > 9 or b > 9:
        print(-1)
    else:
        print(a * b)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a <= 9 and b <= 9:
        print(a * b)
    else:
        print(-1)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if 1 <= a <= 20 and 1 <= b <= 20:
        print(a * b)
    else:
        print(-1)

=======
Suggestion 4

def main():
    # input
    A, B = map(int, input().split())

    # compute

    # output
    if A > 9 or B > 9:
        print(-1)
    else:
        print(A * B)

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    if A > 9 or B > 9:
        print(-1)
    else:
        print(A * B)

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    if a > 9 or b > 9:
        print('-1')
    else:
        print(a*b)

=======
Suggestion 7

def main():
    a,b = map(int, input().split())
    if a < 1 or a > 20 or b < 1 or b > 20:
        return
    print(a*b)
    return
