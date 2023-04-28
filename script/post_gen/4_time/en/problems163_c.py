Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in a:
        b[i-1] += 1
    for i in b:
        print(i)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n-1):
        b[a[i]-1] += 1
    for i in range(n):
        print(b[i])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(1, N):
        B[A[i-1]-1] += 1
    for i in range(N):
        print(B[i])

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

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    for i in a:
        ans[i - 1] += 1
    for i in ans:
        print(i)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N - 1):
        B[A[i]] += 1
    for i in range(1, N + 1):
        print(B[i])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0]*N
    for i in A:
        B[i-1] += 1
    for i in B:
        print(i)
main()

=======
Suggestion 8

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [0] * n
    for i in range(n-1):
        b[a[i]-1] += 1
    for i in range(n):
        print(b[i])

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    subordinate = [0] * n
    for i in range(n - 1):
        subordinate[a[i] - 1] += 1
    for i in subordinate:
        print(i)

=======
Suggestion 10

def main():
    n=int(input())
    A=list(map(int,input().split()))
    B=[0]*n
    for i in range(len(A)):
        B[A[i]-1]+=1
    for i in range(len(B)):
        print(B[i])
