Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i):
            ans += (A[i] - A[j]) ** 2
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ans += (a[i] - a[j]) ** 2
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    for i in range(n):
        for j in range(i):
            s += (a[i] - a[j]) ** 2
    print(s)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        for j in range(i):
            sum += (A[i] - A[j]) ** 2
    print(sum)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans += (A[i]-A[j])**2
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum += (A[i] - A[j]) ** 2
    print(sum)

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [0]*(N+1)
    for i in range(N):
        B[i+1] = B[i] + A[i]
    ans = 0
    for i in range(N):
        ans += (N-i-1)*A[i]**2 - 2*A[i]*(B[N]-B[i+1]) + (B[N]-B[i+1])**2
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A2 = [a**2 for a in A]
    A3 = [a**3 for a in A]
    A4 = [a**4 for a in A]
    A2_sum = sum(A2)
    A3_sum = sum(A3)
    A4_sum = sum(A4)
    ans = 0
    for i in range(N):
        ans += (i*A2[i] - A3_sum)
        ans += (A2_sum - (N-i-1)*A2[i])
        A2_sum -= A2[i]
        A3_sum -= A3[i]
    print(ans)
