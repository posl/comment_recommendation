Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] < L:
            ans += L
        elif A[i] > R:
            ans += R
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 2

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    print(sum(A[:N//2]) * L + sum(A[N//2:]) * R)

=======
Suggestion 3

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if i < N // 2:
            ans += min(A[i], L)
        else:
            ans += min(A[i], R)
    print(ans)

=======
Suggestion 4

def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        if a[i] < l:
            b[i] = l
        elif a[i] > r:
            b[i] = r
        else:
            b[i] = a[i]
    print(sum(b))

main()

=======
Suggestion 5

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    print(sum(A[:N//2])+L*(N//2)+R*(N-N//2))

=======
Suggestion 6

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = max(A[i], L)
        B[i] = min(B[i], R)
    print(sum(B))

=======
Suggestion 7

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if L > 0:
        print(sum(A) + (N - 1) * L)
    elif R < 0:
        print(sum(A) + (N - 1) * R)
    else:
        print(sum(A[:N // 2]) + L * (N // 2) + R * (N - N // 2))

=======
Suggestion 8

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse = True)
    B = []
    for i in range(N):
        if A[i] >= 0:
            B.append(A[i])
        else:
            break
    B.sort()
    C = []
    for i in range(N):
        if A[i] < 0:
            C.append(A[i])
        else:
            break
    C.sort(reverse = True)
    D = B + C
    for i in range(len(D)):
        if D[i] >= 0:
            D[i] = min(D[i], R)
        else:
            D[i] = max(D[i], L)
    print(sum(D))

=======
Suggestion 9

def main():
    from sys import stdin
    from collections import deque
    readline = stdin.readline

    N, L, R = map(int, readline().split())
    A = list(map(int, readline().split()))
    A = deque(A)

    ans = 0
    if L >= 0:
        ans = sum(A)
        ans += N * L
    elif R <= 0:
        ans = sum(A)
        ans += N * R
    else:
        for i in range(N):
            if A[i] >= 0:
                ans += A[i]
                A[i] = 0
            else:
                ans += R
                A[i] = R

        for i in range(N):
            if A[i] == 0:
                continue

            if L >= 0:
                ans += L
            else:
                ans += A[i]
                A[i] = 0

            for j in range(i+1, N):
                if A[j] == 0:
                    continue
                else:
                    ans += A[j]
                    A[j] = 0
                    break

    print(ans)

=======
Suggestion 10

def main():
    # Read input
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))

    # Initialize
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]

    # Compute
    ans = 10 ** 20
    for i in range(N + 1):
        if L * i <= S[i] <= R * i:
            ans = min(ans, S[i] + max(0, L * (N - i) - S[N] + S[i]))
            ans = min(ans, S[i] + max(0, R * (N - i) - S[N] + S[i]))
    print(ans)
