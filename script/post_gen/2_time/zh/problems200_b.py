Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problem200_b(n, k):
    for i in range(k):
        if n % 200 == 0:
            n = n // 200
        else:
            n = int(str(n) + "200")
    print(n)

=======
Suggestion 2

def problem200_b(n,k):
    if k == 0:
        return n
    if n % 200 == 0:
        return problem200_b(n//200,k-1)
    else:
        return problem200_b(int(str(n)+"200"),k-1)

=======
Suggestion 3

def problem200_b(n,k):
    for i in range(k):
        if n%200 == 0:
            n = n//200
        else:
            n = int(str(n) + '200')
    return n

=======
Suggestion 4

def f1(n,k):
    for i in range(k):
        if n%200==0:
            n=n//200
        else:
            n=int(str(n)+'200')
    return n

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    for i in range(k):
        if n % 200 == 0:
            n = n // 200
        else:
            n = int(str(n) + "200")
    print(n)

=======
Suggestion 6

def func(N,K):
    for i in range(K):
        if N%200==0:
            N=N//200
        else:
            N=str(N)
            N=N+'200'
            N=int(N)
    return N

=======
Suggestion 7

def calculate(N, K):
    if K == 0:
        return N
    if N % 200 == 0:
        return calculate(N // 200, K - 1)
    else:
        return calculate(N * 1000 + 200, K - 1)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    for i in range(k):
        if n % 200 == 0:
            n = n / 200
        else:
            n = int(str(n) + '200')
    print(int(n))

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    for i in range(K):
        if N%200 == 0:
            N = N//200
        else:
            N = int(str(N)+'200')
    print(N)
