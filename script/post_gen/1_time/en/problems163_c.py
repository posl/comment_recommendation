Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for a in A:
        B[a-1] += 1
    for b in B:
        print(b)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    subordinates = [0] * N
    for i in range(N-1):
        subordinates[A[i]-1] += 1
    for i in range(N):
        print(subordinates[i])

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] += 1
    for i in range(n):
        print(b[i])

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0] * n
    for i in range(n-1):
        c[a[i]-1] += 1
    for i in c:
        print(i)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = [0] * (N+1)
    for i in range(N-1):
        count[A[i]] += 1
    for i in range(1, N+1):
        print(count[i])

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    b = [0] * (n + 1)
    for i in range(n, 0, -1):
        b[a[i]] += b[i] + 1
    for i in range(1, n + 1):
        print(b[i])

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    count = [0] * n
    for i in range(n):
        count[a[i]-1] += 1
    for i in range(n):
        print(count[i])

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    subordinates = [0] * (n+1)
    for i in range(2, n+1):
        subordinates[a[i-1]] += 1
    for i in range(1, n+1):
        print(subordinates[i])

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    B = [0] * N
    for i in range(N-1):
        B[A[i]-1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int,input().split()))
    #print(N)
    #print(A)
    B = [0]*N
    #print(B)
    for i in range(N-1):
        B[A[i]-1] += 1
    for i in range(N):
        print(B[i])
