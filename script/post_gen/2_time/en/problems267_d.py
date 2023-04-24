Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = (A[i], i)
    B.sort(key=lambda x: x[0], reverse=True)
    ans = 0
    for i in range(M):
        ans += (i+1) * B[i][0]
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0]*(N+1)
    for i in range(N):
        B[i+1] = B[i] + A[i]
    ans = 0
    for i in range(M, N+1):
        for j in range(N-i+1):
            ans = max(ans, B[i+j]-B[j])
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - (i + 1)
    B.sort()
    ans = sum(A[:M])
    for i in range(M):
        ans += B[i]
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    print(sum(A[:M]))

main()

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = (A[i], i)
    B.sort(reverse=True)
    ans = 0
    for i in range(M):
        ans += (i + 1) * B[i][0]
    print(ans)

solve()

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = A[::-1]
    ans = 0
    for i in range(M):
        ans += (i+1) * A[i]
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] + sorted([A[i] - A[i - 1] for i in range(1, N)])
    print(sum(B[-M:]))

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    B = []
    for i in range(N):
        B.append(A[i] + i + 1)
    B.sort(reverse=True)
    print(sum(B[0:M]))

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a + 1 for a in A]
    A.sort(reverse=True)
    print(sum(A[:M]))

=======
Suggestion 10

def solve(n, m, a):
    a = sorted(a, reverse=True)
    total = sum(a[:m])
    return total + m * m
