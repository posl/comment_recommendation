Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if A <= B:
        print(B - A + 1)
    else:
        print(0)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())

    if a > b:
        print(0)
    else:
        print(b - a + 1)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print(b - a + 1 if a <= b else 0)

=======
Suggestion 4

def main():
    # input
    a, b = map(int, input().split())

    # compute

    # output
    print(max(0, b-a+1))

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    print(b-a+1 if b-a >= 0 else 0)

=======
Suggestion 6

def main():
    # input
    a,b = map(int, input().split())
    # compute
    cnt = 0
    for i in range(a, b+1):
        cnt += 1
    # output
    print(cnt)

=======
Suggestion 7

def solve():
    a, b = map(int, input().split())
    print(max(0, b - a + 1))
solve()

=======
Suggestion 8

def solve(a,b):
    if a > b:
        return 0
    else:
        return b-a+1
