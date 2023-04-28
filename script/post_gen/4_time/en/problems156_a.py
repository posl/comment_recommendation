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
    N, R = map(int, input().split())
    if N >= 10:
        print(R)
    else:
        print(R + 100 * (10 - N))

=======
Suggestion 3

def inner_rating(n, r):
    if n >= 10:
        return r
    else:
        return r + 100 * (10 - n)

=======
Suggestion 4

def innerRating(N, R):
    if N >= 10:
        return R
    else:
        return R + 100 * (10 - N)

=======
Suggestion 5

def problems156_a():
    N,R = map(int,input().split())
    if N >= 10:
        print(R)
    else:
        print(R + 100 * (10 - N))

=======
Suggestion 6

def innerRating(n, r):
    if n < 10:
        return r - 100 * (10 - n)
    else:
        return r

=======
Suggestion 7

def innerRating(n,r):
    if n >= 10:
        print(r)
    else:
        print(r + 100 * (10 - n))

innerRating(2,2919)
innerRating(22,3051)
