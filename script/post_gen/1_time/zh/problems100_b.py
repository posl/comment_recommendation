Synthesizing 10/10 solutions

=======
Suggestion 1

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
    else:
        if N == 100:
            print(1010000)
        else:
            print(N*10000)

=======
Suggestion 2

def find_num(D, N):
    if D == 0:
        return N
    elif D == 1:
        return N * 100
    else:
        return N * 10000

D, N = map(int, input().split())
print(find_num(D, N))

=======
Suggestion 3

def main():
    D, N = map(int, input().split())
    if N == 100:
        N = 101
    print(100**D*N)

=======
Suggestion 4

def myfun():
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
            print(100*n)
    else:
        if n == 100:
            print(1010000)
        else:
            print(10000*n)

=======
Suggestion 5

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

=======
Suggestion 6

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
Suggestion 7

def find_number(d, n):
    if d == 0:
        return n
    elif d == 1:
        return n * 100
    else:
        return n * 10000

d, n = map(int, input().split())
print(find_number(d, n))

=======
Suggestion 8

def solve():
    d, n = map(int, input().split())
    print((100**d)*n if n < 100 else (100**d)*(n+1))

=======
Suggestion 9

def main():
    D,N = input().split()
    D = int(D)
    N = int(N)
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

main()

=======
Suggestion 10

def getNthMinNumDivisibleBy100(D,N):
    #D是0，1或2。N是1到100（包括）之间的整数。
    #能被100整除D次的整数如下：
    #D=0 1, 2, 3, 4, 5, 6, 7, ...
    #D=1 100, 200, 300, 400, 500, 600, 700, 800, 900, 1 000, 1 100, ...
    #D=2 10 000, 20 000, 30 000, ...
    if D==0:
        return N
    elif D==1:
        return N*100
    elif D==2:
        return N*10000
