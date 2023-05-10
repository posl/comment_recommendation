Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    for i in range(k):
        if n%200 == 0:
            n = n//200
        else:
            n = int(str(n)+"200")
    print(n)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    for i in range(1,K+1):
        if N % 200 == 0:
            N = N // 200
        else:
            N = int(str(N) + "200")
    print(N)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    for i in range(k):
        if n % 200 == 0:
            n = n // 200
        else:
            n = int(str(n) + '200')
    print(n)

=======
Suggestion 4

def main():
    # input
    N, K = map(int, input().split())

    # compute
    for _ in range(K):
        if N % 200 == 0:
            N //= 200
        else:
            N = int(str(N) + '200')

    # output
    print(N)

=======
Suggestion 5

def main():
    N,K = map(int,input().split())
    for i in range(K):
        if N%200 == 0:
            N = N//200
        else:
            N = int(str(N) + "200")
    print(N)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    for i in range(K):
        if N%200 == 0:
            N = int(N/200)
        else:
            N = int(str(N)+str(200))
    print(N)

=======
Suggestion 7

def problems200_b():
    N, K = map(int, input().split())
    for _ in range(K):
        if N % 200 == 0:
            N //= 200
        else:
            N = int(str(N) + '200')
    return N

print(problems200_b())

=======
Suggestion 8

def solve(N, K):
    for i in range(K):
        if N%200==0:
            N = N//200
        else:
            N = int(str(N) + "200")
    return N
