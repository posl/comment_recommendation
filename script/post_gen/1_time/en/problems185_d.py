Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if M == 0:
        print(1)
        return
    A.sort()
    A = [0] + A + [N + 1]
    B = []
    for i in range(M + 1):
        B.append(A[i + 1] - A[i] - 1)
    B.sort()
    B = B[::-1]
    k = B[0]
    for i in range(1, M + 1):
        k = gcd(k, B[i])
    print((B[0] + k - 1) // k)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(0)
    A.append(N+1)
    A.sort()
    if M == 0:
        print(1)
        return
    if M == N:
        print(0)
        return
    B = []
    for i in range(M+1):
        if A[i+1]-A[i]-1 > 0:
            B.append(A[i+1]-A[i]-1)
    if len(B) == 0:
        print(0)
        return
    k = min(B)
    for i in range(len(B)):
        B[i] = B[i]//k
        if B[i] == 0:
            B[i] = 1
    print(sum(B))

main()

I got 100 points. The code is pretty straightforward. The idea is to first find the gaps between the blue squares. Then, choose the minimum gap as k. Then, we can use the stamp k times to cover all the gaps.

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if M == 0:
        print(1)
        return

    A.sort()
    A = [0] + A + [N + 1]
    d = [A[i + 1] - A[i] - 1 for i in range(M + 1)]
    d.sort(reverse=True)
    k = d[0]
    if k == 0:
        print(0)
        return

    ans = 0
    for i in range(M + 1):
        if d[i] == 0:
            break
        ans += (d[i] + k - 1) // k
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(N + 1)
    if M == 0:
        print(1)
        return
    if M == N:
        print(0)
        return
    dist = []
    for i in range(M):
        if A[i] + 1 < A[i + 1]:
            dist.append(A[i + 1] - A[i] - 1)
    dist.sort(reverse=True)
    ans = dist[0] + 1
    for i in range(1, M):
        ans = max(ans, (dist[i] - 1) // i + 1)
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A + [N + 1]
    B = []
    for i in range(M + 1):
        B.append(A[i + 1] - A[i] - 1)
    B.sort()
    print(sum(B[:M + 1 - B.count(0)]))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(N+1)
    B = []
    for i in range(M+1):
        if A[i] != 1:
            B.append(A[i]-A[i-1]-1)
    B.sort(reverse=True)
    ans = 0
    for i in range(M):
        if B[i] > 0:
            ans += B[i]
    print(ans)

=======
Suggestion 7

def get_input():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    return N, M, A

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(N+1)
    B = [0]
    for i in range(M):
        B.append(A[i+1] - A[i] - 1)
    B.append(A[0] - 1)
    B.append(N - A[M])
    B.sort()
    ans = 0
    for i in range(len(B)-1):
        ans += B[i]
    print(ans)

=======
Suggestion 9

def solve(N, M, A):
    # N: number of squares
    # M: number of blue squares
    # A: list of blue squares
    # return: minimum number of uses of the stamp needed to have no white square.

    if M == 0:
        return 1

    A = [0] + A + [N + 1]
    B = []
    for i in range(M + 1):
        B.append(A[i + 1] - A[i] - 1)

    maxB = max(B)
    if maxB == 0:
        return 0

    B.sort()
    B = B[1:]

    minB = B[0]
    for i in range(1, M):
        minB = gcd(minB, B[i])

    return (maxB + minB - 1) // minB

=======
Suggestion 10

def  main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(n+1)
    cnt = []
    prev = 0
    for i in range(m+1):
        if a[i] - prev - 1 > 0:
            cnt.append(a[i] - prev - 1)
        prev = a[i]
    if len(cnt) == 0:
        print(0)
        return
    k = min(cnt)
    ans = 0
    for i in range(len(cnt)):
        ans += (cnt[i] - 1) // k + 1
    print(ans)
