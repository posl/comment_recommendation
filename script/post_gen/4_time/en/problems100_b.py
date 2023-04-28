Synthesizing 10/10 solutions (Duplicates hidden)

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
    d,n = map(int,input().split())
    if n == 100:
        if d == 0:
            print(101)
        elif d == 1:
            print(10100)
        elif d == 2:
            print(1010000)
    else:
        if d == 0:
            print(n)
        elif d == 1:
            print(n*100)
        elif d == 2:
            print(n*10000)

=======
Suggestion 3

def main():
    d, n = map(int, input().split())
    if n == 100:
        n = 101
    print(100**d * n)

=======
Suggestion 4

def main():
    d, n = map(int, input().split())
    if n == 100:
        n += 1
    print(100**d * n)

=======
Suggestion 5

def main():
    input_str = input()
    input_list = input_str.split()
    D = int(input_list[0])
    N = int(input_list[1])
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

def main():
    d, n = map(int, input().split())
    if n == 100:
        n = 101
    print(n * 100 ** d)

=======
Suggestion 7

def main():
    D, N = map(int, input().split())
    print(100**D*N)

=======
Suggestion 8

def main():
    D, N = map(int, input().split())
    print(100**D * N if N != 100 else 100**D * (N+1))

main()

=======
Suggestion 9

def main():
    D,N = map(int, input().split())
    print((100**D)*(N+1) if N == 100 else (100**D)*N)
