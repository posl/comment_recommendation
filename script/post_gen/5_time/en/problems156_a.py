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

def problems156_a():
    n, r = map(int, input().split())
    if n >= 10:
        print(r)
    else:
        print(r + 100 * (10 - n))

=======
Suggestion 3

def inner_rating(n, r):
    if n < 10:
        return r - 100 * (10 - n)
    else:
        return r

n, r = map(int, input().split())
print(inner_rating(n, r))

=======
Suggestion 4

def inner_rating(n, r):
    if n >= 10:
        return r
    else:
        return r + 100 * (10 - n)

=======
Suggestion 5

def inner_rating(n, r):
    if n >= 10:
        return r
    else:
        return r - (100 * (10 - n))

n, r = map(int, input().split())
print(inner_rating(n, r))

=======
Suggestion 6

def inner_rating(n, r):
    if n < 10:
        return r - 100 * (10 - n)
    else:
        return r

=======
Suggestion 7

def main():
    n, r = map(int, input().split())
    print(r + 100 * max(0, 10-n))
