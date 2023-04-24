Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int,input().split()))
    sum = 0
    for i in range(N-1):
        for j in range(i+1,N):
            sum += abs(A[i]-A[j])
    print(sum)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += abs(a[i]-a[j])
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * i - A[i] * (N - i - 1)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        ans += (A[i+1]-A[i])*(i+1)*(N-i-1)
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += i * A[i] - (N - i - 1) * A[i]
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += a[i] * (i * (n - i - 1) + (i * (i - 1) // 2) + ((n - i - 1) * (n - i) // 2))
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += (N-1-i)*A[i] - i*A[i]
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    sum = 0
    for i in range(N):
        sum += A[i] * (i - (N - 1 - i))
    print(sum)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int,input().split()))

    if n == 2:
        print(abs(a[0]-a[1]))
        return

    a.sort()
    ans = 0
    for i in range(n):
        ans += (n-i-1)*a[i] - i*a[i]

    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    #print(A)

    ans = 0
    for i in range(1, N):
        ans += (A[i] - A[i-1]) * i * (N-i)

    print(ans)
