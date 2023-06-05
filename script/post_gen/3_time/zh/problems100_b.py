Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problem100_b():
    D,N = map(int,input().split())
    if D == 0:
        if N == 100:
            print(101)
        else:
            print(N)
    elif D == 1:
        if N == 100:
            print(101*100)
        else:
            print(N*100)
    elif D == 2:
        if N == 100:
            print(101*100*100)
        else:
            print(N*100*100)
    else:
        pass

=======
Suggestion 2

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
Suggestion 3

def problems100_b():
    a = input().split()
    d = int(a[0])
    n = int(a[1])
    if d == 0:
        if n == 100:
            print(101)
        else:
            print(n)
    elif d == 1:
        if n == 100:
            print(10100)
        else:
            print(100*n)
    else:
        if n == 100:
            print(1010000)
        else:
            print(10000*n)

problems100_b()

=======
Suggestion 4

def problem100_b():
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
Suggestion 5

def problems100_b():
    d,n = map(int,input().split())
    if n == 100:
        n = 101
    if d == 0:
        print(n)
    elif d == 1:
        print(n*100)
    else:
        print(n*10000)

=======
Suggestion 6

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
    elif D == 2:
        if N == 100:
            print(1010000)
        else:
            print(N * 10000)

=======
Suggestion 7

def problem100_b(D,N):
    if D == 0:
        if N == 100:
            return 101
        else:
            return 100**D * N
    elif D == 1:
        if N == 100:
            return 10001
        else:
            return 100**D * N
    else:
        if N == 100:
            return 1000001
        else:
            return 100**D * N

=======
Suggestion 8

def main():
    d,n = map(int,input().split())
    if d == 0:
        print(n if n != 100 else 101)
    elif d == 1:
        print(n * 100 if n != 100 else 10100)
    else:
        print(n * 10000 if n != 100 else 1010000)

=======
Suggestion 9

def problems100_b():
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
    elif D == 2:
        if N == 100:
            print(1010000)
        else:
            print(N*10000)
