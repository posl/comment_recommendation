Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, R = map(int, input().split())
    if N >= 10:
        print(R)
    else:
        print(R + 100 * (10 - N))

=======
Suggestion 2

def main():
    n, r = map(int, input().split())
    if n >= 10:
        print(r)
    else:
        print(r + 100 * (10 - n))

=======
Suggestion 3

def main():
    N, R = map(int, input().split())
    if N >= 10:
        print(R)
    else:
        print(R + (100 * (10 - N)))

=======
Suggestion 4

def main():
    n, r = map(int, input().split())
    if n >= 10:
        print(r)
    else:
        print(r + (100 * (10 - n)))

=======
Suggestion 5

def main():
    N, R = [int(x) for x in input().split()]
    if N >= 10:
        print(R)
    else:
        print(R + 100 * (10 - N))

=======
Suggestion 6

def main():
    N, R = map(int, input().split())
    print(R + 100 * (10 - N) if N < 10 else R)

=======
Suggestion 7

def main():
    n, r = map(int, input().split())
    print(r + 100 * max(0, 10 - n))

=======
Suggestion 8

def main():
    n, r = map(int, input().split())
    print(r + max(100 * (10 - n), 0))
