Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    p, q, r = map(int, input().split())
    print(min(p + q, q + r, r + p))

=======
Suggestion 2

def min_time(p,q,r):
    return min(p+q,min(q+r,p+r))

=======
Suggestion 3

def get_min_time(P, Q, R):
    min_time = P + Q
    if min_time > Q + R:
        min_time = Q + R
    if min_time > R + P:
        min_time = R + P
    return min_time

=======
Suggestion 4

def solve():
    p, q, r = map(int, input().split())
    print(min(p + q, q + r, r + p))

=======
Suggestion 5

def main():
    a = input().split()
    p = int(a[0])
    q = int(a[1])
    r = int(a[2])
    print(min(p+q,q+r,r+p))

=======
Suggestion 6

def min(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

=======
Suggestion 7

def min_time(p,q,r):
    return min(p+q, q+r, r+p)
