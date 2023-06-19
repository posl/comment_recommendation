Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(N, A):
    if N == 1:
        if A[0] == 1:
            return 0
        else:
            return -1
    else:
        if A[0] != 1:
            return -1
        else:
            for i in range(1, N):
                if A[i] - A[i-1] > 1:
                    return -1
            return N - 1

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    # print(N)
    # print(A)

    ans = 0
    for i in range(N):
        if A[i] == i + 1:
            ans += 1
    if ans == N:
        ans = 0
    elif ans == N - 1:
        ans = 1
    else:
        ans = N - ans
    print(ans)

=======
Suggestion 4

def solve(n, a):
    if n == 1 and a[0] == 1:
        return 0
    if n == 1 and a[0] != 1:
        return -1
    if n > 1 and a[0] != 1:
        return -1
    if n > 1 and a[0] == 1:
        for i in range(1, n):
            if a[i] - a[i-1] != 1:
                return i
        return n - 1

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [a[i] - 1 for i in range(n)]
    cnt = 0
    for i in range(n):
        if i == a[a[i]]:
            cnt += 1
    if cnt == n:
        print(0)
        exit()
    for i in range(n):
        if i == a[a[i]]:
            cnt -= 1
        if i == a[i]:
            cnt += 1
    print(cnt // 2)

=======
Suggestion 6

def solve():
    N = int(input())
    A = map(int, input().split())
    ans = 0
    for i, a in enumerate(A, 1):
        if i != a:
            ans += 1
    if ans == N:
        ans = -1
    print(ans)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] == i + 1:
            ans += 1
    if ans == N:
        print(0)
    elif ans == N - 1:
        print(1)
    else:
        print(N - ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i + 1
    ans = 0
    for i in range(N - 1):
        if B[i] > B[i + 1]:
            ans += 1
    print(ans + 1)

=======
Suggestion 9

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if A[0] != 1:
        return -1
    if N == 1:
        return 0
    ans = 0
    for i in range(N - 1):
        if A[i] + 1 == A[i + 1]:
            ans += 1
        elif A[i] < A[i + 1]:
            return -1
        else:
            ans += A[i + 1]
    return ans

print(solve())

=======
Suggestion 10

def solve():
    pass
