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
        for j in range(i):
            ans += (a[i] - a[j]) ** 2
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        for j in range(i):
            ans += (A[i] - A[j]) ** 2
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            ans += (A[i] - A[j]) ** 2
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        for j in range(i):
            sum += (A[i]-A[j])**2
    print(sum)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    sumA = sum(A)
    for i in range(N):
        sumA -= A[i]
        ans += A[i]**2 * (N-1) - 2 * A[i] * sumA
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(i) for i in input().split()]

    sum = 0
    for i in range(n):
        for j in range(i):
            sum += (a[i] - a[j])**2

    print(sum)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int,input().split()))
    print(sum([sum([(a[i]-a[j])**2 for j in range(i)]) for i in range(1,n)]))

=======
Suggestion 9

def main():
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range(n):
        ans+=a[i]*a[i]*(n-1)
        for j in range(i+1,n):
            ans-=2*a[i]*a[j]
    print(ans)
