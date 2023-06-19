Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, r = map(int, input().split())
    if n < 10:
        print(r + 100 * (10 - n))
    else:
        print(r)

=======
Suggestion 2

def main():
    n, r = map(int, input().split())
    if n < 10:
        print(r + (100 * (10 - n)))
    else:
        print(r)

=======
Suggestion 3

def getInnerRank(n, r):
    if n >= 10:
        return r
    else:
        return r + 100 * (10 - n)

=======
Suggestion 4

def main():
    n,r = map(int,raw_input().split())
    if n < 10:
        print r + 100*(10-n)
    else:
        print r

=======
Suggestion 5

def main():
    n, r = map(int, input().split())
    if n >= 10:
        print(r)
    else:
        print(r + 100 * (10 - n))

=======
Suggestion 6

def inner_score(n,r):
    if n >= 10:
        return r
    else:
        return r + 100 * (10 - n)

=======
Suggestion 7

def func():
    N,R = map(int,input().split())
    if N < 10:
        print(R + 100*(10-N))
    else:
        print(R)

func()

=======
Suggestion 8

def main():
    n,r = map(int,input().split())
    if n >= 10:
        print(r)
    else:
        print(r+(100*(10-n)))

=======
Suggestion 9

def main():
    N,R = map(int, input().split())
    if N >= 10:
        print(R)
    else:
        print(R + 100 * (10 - N))
