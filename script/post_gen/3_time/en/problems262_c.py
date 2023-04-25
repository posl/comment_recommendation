Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if a[i] == i + 1:
            ans += 1
    print(ans // 2)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] == i+1:
            ans += 1
    print(ans//2)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] == i+1:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if a[i] == i + 1:
            count += 1
    print(count // 2)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    ans = 0
    for i in range(1, N+1):
        if A[i] == i:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N+1):
        left = bisect_left(A, i)
        right = bisect_right(A, i)
        ans += (right - left) * (right - left - 1) // 2
    print(ans)

=======
Suggestion 7

def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    for i in range(N-1):
        if A[i] == i+1:
            ans += 1
        elif A[i] < i+1 and A[i+1] > i+1:
            ans += 1
    if A[N-1] == N:
        ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.insert(0,0)
    A.insert(0,0)
    A.insert(N+3,0)
    A.insert(N+3,0)
    cnt = 0
    for i in range(2,N+2):
        if A[i-1] == i-1 and A[i+1] == i+1:
            cnt += 1
    for i in range(2,N+2):
        if A[i-1] == i+1 and A[i+1] == i-1:
            cnt += 1
    print(cnt)

=======
Suggestion 9

def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    A = [0] + A

    # i = 1, 2, ..., N
    # min(A[i], A[j]) = i
    # max(A[i], A[j]) = j
    # i < j

    # A[i] が i であるものの個数
    count = [0] * (N + 1)
    for i in range(1, N + 1):
        count[A[i]] += 1

    # A[j] が j であるものの個数
    count2 = [0] * (N + 1)
    for j in range(1, N + 1):
        count2[A[j]] += 1

    # A[i] が i であるものの個数
    # A[j] が j であるものの個数
    # の積
    ans = 0
    for i in range(1, N + 1):
        ans += count[i] * count2[i]

    print(ans)
