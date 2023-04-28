Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if M == 0:
        print(1)
        return
    if N == M:
        print(0)
        return
    diff = []
    for i in range(M):
        if i == 0:
            diff.append(A[i] - 1)
        else:
            diff.append(A[i] - A[i - 1] - 1)
    diff.append(N - A[M - 1])
    diff.sort()
    diff.reverse()
    k = diff[0]
    count = 0
    for i in range(M + 1):
        count += (diff[i] + k - 1) // k
    print(count)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if M == 0:
        print(1)
        return
    if N == M:
        print(0)
        return
    B = []
    for i in range(M):
        if i == 0:
            B.append(A[i]-1)
        else:
            B.append(A[i]-A[i-1]-1)
        if i == M-1:
            B.append(N-A[i])
    B.sort()
    k = B[0]
    ans = 0
    for i in range(len(B)):
        if B[i]%k == 0:
            ans += B[i]//k
        else:
            ans += B[i]//k + 1
    print(ans)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if m == 0:
        print(1)
        return
    if n == m:
        print(0)
        return
    d = []
    for i in range(m-1):
        d.append(a[i+1]-a[i]-1)
    d.sort()
    k = a[0]-1
    if k > 0:
        d.append(k)
    k = n-a[-1]
    if k > 0:
        d.append(k)
    k = d[0]
    ans = 0
    for i in range(len(d)):
        ans += (d[i]+k-1)//k
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if M == 0:
        print(1)
        exit()
    if N == M:
        print(0)
        exit()
    diff = []
    for i in range(1, M):
        diff.append(A[i] - A[i-1] - 1)
    diff.sort()
    ans = 0
    for i in range(M - N + 1):
        ans += diff[i]
    print(ans + 1)

main()

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(0)
    A.append(N+1)
    A.sort()
    B = []
    for i in range(M+1):
        if A[i+1] - A[i] > 1:
            B.append(A[i+1] - A[i] - 1)
    if len(B) == 0:
        print(0)
    else:
        k = min(B)
        ans = 0
        for i in range(len(B)):
            ans += (B[i]+k-1)//k
        print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    if M == 0:
        print(1)
        exit()

    if N == M:
        print(0)
        exit()

    B = []
    for i in range(M-1):
        B.append(A[i+1] - A[i] - 1)
    B.sort()
    B.reverse()

    if N == 1:
        print(0)
        exit()

    print(sum(B) + N - M - 1)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(1)
        return

    A = sorted(list(map(int, input().split())))

    if A[0] != 1:
        A.insert(0, 0)
    if A[-1] != N:
        A.append(N+1)

    if len(A) == 2:
        print(1)
        return

    # print(A)

    diff = []
    for i in range(1, len(A)):
        diff.append(A[i]-A[i-1]-1)

    # print(diff)

    k = min(diff)
    res = 0
    for i in range(len(diff)):
        res += diff[i]//k
        if diff[i]%k != 0:
            res += 1

    print(res)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    if m == 0:
        print(1)
        return
    a = list(map(int, input().split()))
    a.sort()
    b = []
    b.append(a[0]-1)
    for i in range(1, m):
        b.append(a[i]-a[i-1]-1)
    b.append(n-a[m-1])
    b.sort()
    k = b[0]
    ans = 0
    for i in range(m+1):
        if b[i] % k == 0:
            ans += b[i] // k
        else:
            ans += b[i] // k + 1
    print(ans)

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    if m == 0:
        print(1)
        return
    a = list(map(int,input().split()))
    a.sort()
    white = []
    for i in range(m):
        if i == 0:
            white.append(a[i]-1)
        else:
            white.append(a[i]-a[i-1]-1)
        if i == m-1:
            white.append(n-a[i])
    white.sort()
    if white[0] == 0:
        print(0)
        return
    k = white[0]
    count = 0
    for i in range(m):
        count += (a[i]+k-1)//k
    print(count)

=======
Suggestion 10

def get_input():
    return map(int, input().strip().split())
