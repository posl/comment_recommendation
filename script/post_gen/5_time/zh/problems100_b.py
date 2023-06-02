Synthesizing 10/10 solutions

=======
Suggestion 1

def get_num(d, n):
    if d == 0:
        return n
    elif d == 1:
        return n * 100
    elif d == 2:
        return n * 10000

=======
Suggestion 2

def getNthMinNum(D,N):
    if D == 0:
        return N
    elif D == 1:
        return N * 100
    elif D == 2:
        return N * 10000

=======
Suggestion 3

def solution():
    D, N = map(int, input().split())
    if D == 0:
        if N == 100:
            print(101)
        else:
            print(N)
    elif D == 1:
        if N == 100:
            print(10100)
        else:
            print(N * 100)
    else:
        if N == 100:
            print(1010000)
        else:
            print(N * 10000)

=======
Suggestion 4

def getNum(d, n):
    if d == 0:
        return n
    elif d == 1:
        return n * 100
    else:
        return n * 10000

=======
Suggestion 5

def main():
    D, N = map(int, input().split())
    if D == 0:
        if N == 100:
            print(101)
        else:
            print(N)
    elif D == 1:
        if N == 100:
            print(10100)
        else:
            print(N*100)
    else:
        if N == 100:
            print(1010000)
        else:
            print(N*10000)

=======
Suggestion 6

def get_num(D, N):
    if D == 0:
        return N
    elif D == 1:
        return N * 100
    else:
        return N * 10000

=======
Suggestion 7

def solve(d,n):
    if d == 0:
        if n == 100:
            return 101
        else:
            return n
    elif d == 1:
        if n == 100:
            return 10100
        else:
            return 100*n
    else:
        if n == 100:
            return 1010000
        else:
            return 10000*n

=======
Suggestion 8

def get_num(d, n):
    if d == 0:
        return 100**d * n
    elif d == 1:
        return 100**d * n
    elif d == 2:
        return 100**d * n

=======
Suggestion 9

def func():
    d, n = map(int, input().split())
    if d == 0:
        if n == 100:
            print(101)
        else:
            print(n)
    elif d == 1:
        if n == 100:
            print(10100)
        else:
            print(n * 100)
    elif d == 2:
        if n == 100:
            print(1010000)
        else:
            print(n * 10000)

=======
Suggestion 10

def problems100_b():
    d,n = map(int, input().split())
    if d == 0:
        print(n if n < 100 else 101**n)
    elif d == 1:
        print(n*100 if n < 100 else 10100**n)
    else:
        print(n*10000 if n < 100 else 1010000**n)
