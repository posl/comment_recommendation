Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, r = map(int, input().split())
    if n >= 10:
        print(r)
    else:
        print(r + 100 * (10 - n))

=======
Suggestion 2

def main():
    n, r = map(int, input().split())
    if n < 10:
        print(r + 100 * (10 - n))
    else:
        print(r)

=======
Suggestion 3

def main():
    n, r = map(int, input().split(' '))
    print(r + 100 * (10 - min(n, 10)))

=======
Suggestion 4

def calc_internal_rating(n, r):
    if n < 10:
        return r + 100 * (10 - n)
    else:
        return r

=======
Suggestion 5

def main():
    N, R = map(int, input().split())
    if N >= 10:
        print(R)
    else:
        print(R + 100 * (10 - N))

=======
Suggestion 6

def main():
    N, R = map(int, input().split())
    if N <= 10:
        print(R + 100 * (10 - N))
    else:
        print(R)
