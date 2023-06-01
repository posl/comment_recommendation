Synthesizing 10/10 solutions

=======
Suggestion 1

def problem200_b(n,k):
    for i in range(k):
        if n%200 == 0:
            n = int(n/200)
        else:
            n = int(str(n) + "200")
    return n

=======
Suggestion 2

def solve(n,k):
    for i in range(k):
        if n%200==0:
            n=n//200
        else:
            n=int(str(n)+'200')
    return n

n,k=map(int,input().split())
print(solve(n,k))

=======
Suggestion 3

def solve(n,k):
    for _ in range(k):
        if n%200==0:
            n=n//200
        else:
            n=int(str(n)+'200')
    return n

=======
Suggestion 4

def main():
    #输入
    N,K = map(int,input().split())
    for i in range(K):
        if N%200 == 0:
            N = N//200
        else:
            N = int(str(N)+'200')
    print(N)

=======
Suggestion 5

def problems200_b():
    n,k = map(int,input().split())
    for i in range(k):
        if n % 200 == 0:
            n = n // 200
        else:
            n = int(str(n) + "200")
    print(n)

=======
Suggestion 6

def problem200_b(n, k):
    for i in range(k):
        if n % 200 == 0:
            n = n // 200
        else:
            n = int(str(n) + "200")
    return n

=======
Suggestion 7

def func(N,K):
    for i in range(K):
        if N%200 == 0:
            N = N//200
        else:
            N = int(str(N)+"200")
    return N

=======
Suggestion 8

def func(n,k):
    for i in range(k):
        if n % 200 == 0:
            n = n // 200
        else:
            n = int(str(n) + '200')
    return n

=======
Suggestion 9

def solve(n, k):
    for i in range(k):
        if n % 200 == 0:
            n = n // 200
        else:
            n = int(str(n) + "200")
    return n

=======
Suggestion 10

def problem_200_b(n, k):
    for i in range(k):
        if n % 200 == 0:
            n = n // 200
        else:
            n = int(str(n) + '200')
    return n
