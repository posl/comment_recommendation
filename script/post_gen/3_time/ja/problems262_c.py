Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n+1):
        if a[i-1] >= i:
            ans += 1
    print(ans)

main()

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i, a in enumerate(A):
        if i + 1 == a:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(1, N+1):
        if i == A[i-1]:
            cnt += 1
    print(cnt)

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > i+1:
            continue
        for j in range(i+1, N):
            if A[j] < j+1:
                continue
            if A[i] == i+1 and A[j] == j+1:
                ans += 1
    print(ans)
    return 0

=======
Suggestion 5

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0] * n
    for i in range(n):
        c[i] = a[i] - i - 1
    c.sort()
    ans = 0
    for i in range(n):
        if i == 0 or c[i] != c[i - 1]:
            continue
        cnt = 0
        while i < n and c[i] == c[i - 1]:
            i += 1
            cnt += 1
        ans += cnt * (cnt - 1) // 2
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        if a[i] < a[i-1]:
            ans += 1
    print(ans+1)

main()

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > i + 1:
            continue
        if i + 1 > A[A[i] - 1]:
            continue
        if i + 1 == A[A[i] - 1]:
            ans += 1
    print(ans)

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i, a in enumerate(A):
        if a > i + 1:
            continue
        if A[a - 1] == i + 1:
            ans += 1
    print(ans)

=======
Suggestion 9

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    # 1 <= i < j <= N
    # min(a_i, a_j) = i
    # max(a_i, a_j) = j
    # 1 <= a_i <= N
    # 1 <= i <= N
    # 1 <= j <= N
    # 1 <= a_j <= N
    # 1 <=

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    cnt = [0] * (n+1)
    for i in range(n):
        if i + 1 + a[i] <= n:
            cnt[i+1+a[i]] += 1
        if i + 1 - a[i] >= 1:
            ans += cnt[i+1-a[i]]
    print(ans)
