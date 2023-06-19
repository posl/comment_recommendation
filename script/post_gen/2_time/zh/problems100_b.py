Synthesizing 10/10 solutions

=======
Suggestion 1

def problem100_b():
    D, N = map(int, input().split())
    if N == 100:
        N += 1
    print((100 ** D) * N)

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
            print(100 * N)
    else:
        if N == 100:
            print(1010000)
        else:
            print(10000 * N)

=======
Suggestion 3

def problems100_b():
    D, N = map(int, input().split())
    if D == 0:
        print(N if N != 100 else 101)
    elif D == 1:
        print(N * 100 if N != 100 else 10100)
    else:
        print(N * 10000 if N != 100 else 1010000)

=======
Suggestion 4

def getNth(D,N):
    if D == 0:
        print(N)
    elif D == 1:
        print(100*N)
    elif D == 2:
        print(10000*N)
    else:
        print("D is not 0,1,2")

=======
Suggestion 5

def main():
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
    else:
        if n == 100:
            print(1010000)
        else:
            print(n * 10000)

=======
Suggestion 6

def main():
    d, n = map(int, input().split())
    if n != 100:
        print((100 ** d) * n)
    else:
        print((100 ** d) * (n + 1))

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
            print(N*100)
    else:
        if N == 100:
            print(1010000)
        else:
            print(N*10000)
problems100_b()

=======
Suggestion 8

def main():
    #读取输入
    d,n = map(int, input().split())
    #计算
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
Suggestion 9

def main():
    D,N = map(int,input().split())
    if N == 100:
        N = 101
    if D == 0:
        print(N)
    elif D == 1:
        print(N * 100)
    elif D == 2:
        print(N * 10000)

=======
Suggestion 10

def main():
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
    elif d == 2:
        if n == 100:
            print(1010000)
        else:
            print(10000*n)
