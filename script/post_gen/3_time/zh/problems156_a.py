Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

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

def get_inner_grade(n, r):
    if n >= 10:
        return r
    else:
        return r + 100 * (10 - n)

=======
Suggestion 4

def judge(N,R):
    if N>=10:
        return R
    else:
        return R+(10-N)*100

=======
Suggestion 5

def get_inner_score(n, r):
    if n >= 10:
        return r
    else:
        return r + 100 * (10 - n)

=======
Suggestion 6

def main():
    n,r = map(int,input().split())
    if n < 10:
        print(r + 100 * (10 - n))
    else:
        print(r)

=======
Suggestion 7

def inner_score(n, r):
    if n >= 10:
        return r
    else:
        return r + 100 * (10 - n)
