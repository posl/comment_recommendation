Synthesizing 10/10 solutions

=======
Suggestion 1

def sumB(A, N, X):
    B = A * 100
    k = 0
    sumB = 0
    while sumB <= X:
        sumB += B[k]
        k += 1
    return k

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    sum = 0
    for i in range(10 ** 100):
        sum += a[i % n]
        if sum > x:
            print(i + 1)
            break

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    b = a * 10 ** 100
    s = 0
    for i in range(len(b)):
        s += b[i]
        if s > x:
            print(i + 1)
            break

=======
Suggestion 4

def get_input():
    N = int(input())
    A = [int(i) for i in input().split()]
    X = int(input())
    return N,A,X

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    b = a * 100
    sum = 0
    for i in range(len(b)):
        sum += b[i]
        if sum > x:
            print(i+1)
            break

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = A * (10 ** 100)
    sum = 0
    for i in range(len(B)):
        sum += B[i]
        if sum > X:
            print(i + 1)
            break

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = A*100
    s = 0
    for i in range(1, 10**5+1):
        s += B[i-1]
        if s > X:
            print(i)
            break

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    sum = 0
    for i in range(N):
        sum += A[i]
    if sum > X:
        print(N)
    else:
        print((X // sum) * N + N)
main()

=======
Suggestion 10

def solve():
    return 0
