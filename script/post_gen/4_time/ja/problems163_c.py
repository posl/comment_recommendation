Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]*n
    for i in range(n-1):
        b[a[i]-1] += 1
    for i in b:
        print(i)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    for i in range(1, n):
        ans[a[i-1]-1] += 1
    for i in ans:
        print(i)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(1, N):
        ans[A[i-1]-1] += 1
    for i in range(N):
        print(ans[i])

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(1, n):
        b[a[i] - 1] += 1
    for i in range(n):
        print(b[i])

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = [0] * n

    for i in range(1, n):
        ans[a[i-1]-1] += 1

    for i in range(n):
        print(ans[i])

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = [0] * N
    for i in range(N-1):
        ans[A[i]-1] += 1
    for i in ans:
        print(i)

=======
Suggestion 7

def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=[0]*(n+1)
    for i in range(n-1):
        b[a[i]]+=1
    for i in range(1,n+1):
        print(b[i])

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(1, n):
        a[i] -= 1
    ans = [0] * n
    for i in range(1, n):
        ans[a[i]] += 1
    for i in range(n):
        print(ans[i])

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0 for i in range(n)]
    for i in range(1, n):
        ans[a[i-1]-1] += 1
    for i in ans:
        print(i)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (n+1)
    for i in range(1,n):
        b[a[i-1]] += 1
    for i in range(1,n+1):
        print(b[i])
