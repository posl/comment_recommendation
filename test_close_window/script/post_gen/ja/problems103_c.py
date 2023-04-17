Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(sum(A) - N)

=======

def main():
    N = int(input())
    a = list(map(int, input().split()))
    print(sum(a) - N)

=======

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * i - A[i] * (N - i - 1)
    print(ans)

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = [0]*N
    for i in range(N):
        B[i] = A[i] - A[i-1]
    B.sort()
    ans = 0
    for i in range(N):
        ans += B[i]*i
    print(ans)

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    print(sum(A) - N)
