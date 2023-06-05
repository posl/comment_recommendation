Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0,0)
    b = [0]*(n+1)
    for i in range(1,n+1):
        b[a[i]] += 1
    for i in range(1,n+1):
        print(b[i])

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(a)
    b = [0] * n
    for i in range(1, n):
        b[a[i-1]-1] += 1
    for i in b:
        print(i)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n-1):
        b[a[i]-1] += 1
    for i in range(n):
        print(b[i])

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(1, n):
        b[a[i - 1] - 1] += 1
    for i in range(n):
        print(b[i])

main()

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    B = [0 for i in range(N)]
    for i in range(N-1):
        B[A[i]-1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))

    b = [0] * n
    for i in range(1, n):
        b[a[i - 1] - 1] += 1

    for i in range(n):
        print(b[i])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N - 1):
        B[A[i] - 1] += 1
    for i in range(N):
        print(B[i])
