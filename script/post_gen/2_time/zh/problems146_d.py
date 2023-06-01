Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def d(n):
    return len(str(n))

=======
Suggestion 2

def d(n):
    if n < 10:
        return 1
    else:
        return 1 + d(n//10)

=======
Suggestion 3

def d(n):
    if n < 10:
        return 1
    else:
        return d(n//10) + 1

=======
Suggestion 4

def calc_price(a,b,n):
    return a*n+b*len(str(n))

=======
Suggestion 5

def d(N):
    return len(str(N))

=======
Suggestion 6

def d(n):
    return len(str(n))

a,b,x = map(int,input().split())

=======
Suggestion 7

def d(n):
    s = str(n)
    return int(s[0])
