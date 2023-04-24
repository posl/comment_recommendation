Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    b[0] = a[0]
    for i in range(1, n):
        b[i] = max(a[i], b[i - 1])
    ans = 0
    for i in range(n):
        ans += b[i] - a[i]
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1, 0, -1):
        if a[i-1] > a[i]:
            ans += a[i-1] - a[i]
            a[i-1] = a[i]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(1, N):
        if A[i - 1] < A[i]:
            B[i] = B[i - 1] + 1
    print(sum(B))

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - i
    b.sort()
    #print(b)
    ans = 0
    for i in range(n):
        ans += abs(b[i] - b[n//2])
    print(ans)
main()

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - i
    b.sort()
    if n % 2 == 0:
        x = b[n//2-1]
        y = b[n//2]
        ans = y - x + 1
    else:
        ans = b[n//2] * 2 + 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*N
    for i in range(N):
        B[i] = A[i] - i - 1
    B.sort()
    if N%2:
        median = B[N//2]
    else:
        median = (B[N//2-1]+B[N//2])//2
    ans = 0
    for i in range(N):
        ans += abs(B[i]-median)
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1, -1, -1):
        if a[i] > ans:
            ans = a[i]
        else:
            ans = a[i] - 1
        if ans < 0:
            print(-1)
            return
    print(sum(a) - n)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = a[::-1]
    ans = 0
    for i in range(1, n):
        if a[i] > a[i-1]:
            ans += a[i] - a[i-1]
            a[i] = a[i-1]
    print(ans)
main()

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = A[::-1]
    ans = 0
    for i in range(N):
        if A[i] <= ans:
            ans = A[i]
        else:
            ans = A[i] - 1
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(n,a)
    ans = 0
    for i in range(n-1,0,-1):
        if a[i-1] > a[i]:
            ans += a[i-1] - a[i]
            a[i-1] = a[i]
    print(ans)
