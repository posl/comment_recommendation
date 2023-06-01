Synthesizing 10/10 solutions

=======
Suggestion 1

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
            print(N * 100)
    else:
        if N == 100:
            print(1010000)
        else:
            print(N * 10000)

=======
Suggestion 2

def main():
    D,N = map(int,input().split())
    if N == 100:
        N = 101
    print((100**D)*N)

=======
Suggestion 3

def problems100_b():
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
            print(100 * N)
    else:
        if N == 100:
            print(1010000)
        else:
            print(10000 * N)

=======
Suggestion 4

def problems100_b():
    d,n = map(int,input().split())
    if d == 0:
        if n == 100:
            print(101)
        else:
            print(n)
    elif d == 1:
        if n == 100:
            print(10100)
        else:
            print(n*100)
    else:
        if n == 100:
            print(1010000)
        else:
            print(n*10000)

=======
Suggestion 5

def problem100_b():
    D,N = map(int,input().split())
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

def func():
    D,N = map(int,input().split())
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
Suggestion 7

def main():
    D,N = map(int,input().split())
    if N == 100:
        N = 101
    if D == 0:
        print(N)
    elif D == 1:
        print(N*100)
    elif D == 2:
        print(N*10000)

=======
Suggestion 8

def problem100_b(D,N):
    if D == 0:
        print(N)
    elif D == 1:
        print(100*N)
    elif D == 2:
        print(10000*N)

=======
Suggestion 9

def main():
    D,N = map(int,input().split())
    if D == 0:
        if N == 100:
            print(101)
        else:
            print(N)
    elif D == 1:
        if N == 100:
            print(100*101)
        else:
            print(100*N)
    else:
        if N == 100:
            print(100*100*101)
        else:
            print(100*100*N)

=======
Suggestion 10

def findNumber(D, N):
    if D == 0:
        if N == 100:
            return 101
        else:
            return N
    elif D == 1:
        if N == 100:
            return 10100
        else:
            return 100 * N
    else:
        if N == 100:
            return 1010000
        else:
            return 10000 * N
