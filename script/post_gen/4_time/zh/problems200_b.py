Synthesizing 10/10 solutions

=======
Suggestion 1

def problem200_b(n, k):
    for i in range(k):
        if n % 200 == 0:
            n //= 200
        else:
            n = int(str(n) + '200')
    return n

=======
Suggestion 2

def solve(n, k):
    for _ in range(k):
        if n % 200 == 0:
            n //= 200
        else:
            n = int(str(n) + "200")
    return n

n, k = map(int, input().split())
print(solve(n, k))

=======
Suggestion 3

def problem200_b():
    n, k = map(int, input().split())
    for i in range(k):
        if n % 200 == 0:
            n = n // 200
        else:
            n = int(str(n) + '200')
    print(n)

=======
Suggestion 4

def func(n, k):
    for i in range(k):
        if n % 200 == 0:
            n = n // 200
        else:
            n = int(str(n) + '200')
    return n

print(func(2021, 4))
print(func(40000, 2))
print(func(8691, 20))

=======
Suggestion 5

def problem200_b():
    n, k = map(int, input().split())
    for _ in range(k):
        if n % 200 == 0:
            n //= 200
        else:
            n = int(str(n) + "200")
    print(n)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    for _ in range(K):
        if N % 200 == 0:
            N = N // 200
        else:
            N = int(str(N) + '200')
    print(N)

=======
Suggestion 7

def problems200_b():
    N,K = map(int,input().split())
    for i in range(K):
        if N % 200 == 0:
            N = N // 200
        else:
            N = int(str(N) + "200")
    print(N)
problems200_b()

=======
Suggestion 8

def problems200_b():
    n,k = map(int,input().split())
    for i in range(k):
        if n%200 == 0:
            n = n//200
        else:
            n = int(str(n) + '200')
    print(n)

=======
Suggestion 9

def get_input():
    input_line = input()
    n, k = input_line.split()
    return int(n), int(k)

=======
Suggestion 10

def f(n, k):
    for i in range(k):
        if n % 200 == 0:
            n = n / 200
        else:
            n = n * 1000 + 200
    return int(n)
