Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0]*N
    for i in range(N):
        B[i] = A[i] - (i+1)
    B.sort()
    b = B[N//2]
    ans = 0
    for i in range(N):
        ans += abs(A[i] - (b+i+1))
    print(ans)

=======
Suggestion 2

def solve(n, arr):
    arr.sort()
    mid = arr[n//2]
    ans = 0
    for i in range(n):
        ans += abs(arr[i]-mid)
    return ans

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = a[n//2]
    ans = 0
    for i in range(n):
        ans += abs(a[i]-b-i-1)
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [i + 1 - a[i] for i in range(n)]
    b.sort()
    if n % 2 == 1:
        ans = sum(b[n // 2 + 1:]) + sum(b[:n // 2])
    else:
        ans = sum(b[n // 2:]) + sum(b[:n // 2])
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [a[i] - (i + 1) for i in range(n)]
    a.sort()
    b = a[n // 2]
    print(sum(abs(a[i] - b) for i in range(n)))

=======
Suggestion 6

def get_min_sadness(n, a):
    b = 0
    min_sadness = 0
    for i in range(n):
        min_sadness += abs(a[i] - (b + i + 1))
    return min_sadness

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [a[i]-(i+1) for i in range(n)]
    a.sort()
    b = a[n//2]
    print(sum([abs(a[i]-b) for i in range(n)]))

=======
Suggestion 8

def solve():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 10**9
    for b in range(-100,101):
        tmp = 0
        for i in range(n):
            tmp += abs(a[i]-(b+i+1))
        ans = min(ans,tmp)
    print(ans)
solve()

=======
Suggestion 9

def solve(n, arr):
    arr.sort()
    b = arr[n//2]
    ans = 0
    for i in range(n):
        ans += abs(arr[i] - (b+i+1))
    return ans

=======
Suggestion 10

def solve(n, a):
    a.sort()
    b = a[n//2]
    return sum(abs(a[i]-b-i-1) for i in range(n))
