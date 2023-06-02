Synthesizing 10/10 solutions

=======
Suggestion 1

def process(N,K):
    for i in range(K):
        if N % 200 == 0:
            N = N//200
        else:
            N = int(str(N) + '200')
    return N

=======
Suggestion 2

def problem200_b():
    N, K = map(int, input().split())
    for i in range(K):
        if N % 200 == 0:
            N = N // 200
        else:
            N = int(str(N) + "200")
    print(N)

=======
Suggestion 3

def f(n,k):
    if k==0:
        return n
    if n%200==0:
        return f(n//200,k-1)
    else:
        return f(n*1000+200,k-1)

n,k=map(int,input().split())
print(f(n,k))

=======
Suggestion 4

def f(n):
    if n % 200 == 0:
        return n // 200
    else:
        return int(str(n) + '200')

n, k = map(int, input().split())
for i in range(k):
    n = f(n)
print(n)

=======
Suggestion 5

def problems200_b():
    n, k = map(int, input().split())
    for i in range(k):
        if n % 200 == 0:
            n //= 200
        else:
            n = int(str(n) + "200")
    print(n)

=======
Suggestion 6

def problem200_b():
    n, k = map(int, input().split())
    for _ in range(k):
        if n%200 == 0:
            n = n//200
        else:
            n = int(str(n) + "200")
    print(n)

=======
Suggestion 7

def problem200_b(n,k):
    for i in range(k):
        if n%200==0:
            n=n/200
        else:
            n=int(str(n)+"200")
    return n

=======
Suggestion 8

def problems200_b():
    n,k=map(int,input().split())
    for i in range(k):
        if n%200==0:
            n=n//200
        else:
            n=int(str(n)+"200")
    print(n)
problems200_b()

=======
Suggestion 9

def f(n,k):
    for i in range(k):
        if n%200==0:
            n=n//200
        else:
            n=n*1000+200
    return n

n,k=map(int,input().split())
print(f(n,k))

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    for i in range(k):
        if n % 200 == 0:
            n = n // 200
        else:
            n = int(str(n) + "200")
    print(n)
