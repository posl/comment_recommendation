Synthesizing 10/10 solutions

=======
Suggestion 1

def problems100_b(d, n):
    if d == 0:
        return n if n != 100 else 101
    elif d == 1:
        return n * 100 if n != 100 else 10100
    elif d == 2:
        return n * 10000 if n != 100 else 1010000

=======
Suggestion 2

def main():
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

main()

=======
Suggestion 3

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
main()

=======
Suggestion 4

def solution():
    D,N = map(int,input().split())
    if D == 0:
        print(N)
    elif D == 1:
        print(N*100)
    else:
        print(N*10000)

=======
Suggestion 5

def get_number(D,N):
    if D == 0:
        return N
    elif D == 1:
        return N*100
    else:
        return N*10000

D,N = map(int, input().split())
print(get_number(D,N))

=======
Suggestion 6

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
            print(N * 100)
    else:
        if N == 100:
            print(1010000)
        else:
            print(N * 10000)

=======
Suggestion 7

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
            print(100*N)
    else:
        if N == 100:
            print(1010000)
        else:
            print(10000*N)

=======
Suggestion 8

def problems100_b():
    D,N = map(int,input().split())
    if N == 100:
        N = 101
    print(100**D*N)

=======
Suggestion 9

def main():
    D, N = map(int, input().split())
    if N == 100:
        N = 101
    print(100 ** D * N)

=======
Suggestion 10

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
            print(100 * N)
    else:
        if N == 100:
            print(1010000)
        else:
            print(10000 * N)
