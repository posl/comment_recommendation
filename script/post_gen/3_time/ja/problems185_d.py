Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(0)
    A.append(N+1)
    A.sort()
    B = []
    for i in range(M+1):
        B.append(A[i+1]-A[i]-1)
    B.sort()
    B.reverse()
    ans = 0
    for i in range(M+1):
        ans += B[i]*(i+1)
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = []
    for i in range(m):
        if i == 0:
            b.append(a[i]-1)
        else:
            b.append(a[i]-a[i-1]-1)
    if m > 0:
        b.append(n-a[m-1])
    b.sort()
    ans = 0
    for i in range(m+1):
        if b[i] > 0:
            ans += b[i]
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A + [N+1]
    A.sort()
    B = [A[i+1] - A[i] - 1 for i in range(M+1)]
    B = [i for i in B if i != 0]
    k = min(B)
    print((sum(B) + k - 1) // k)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = [0] + a + [n + 1]
    b = []
    for i in range(m + 1):
        b.append(a[i + 1] - a[i] - 1)
    k = min(b)
    ans = 0
    for i in range(m + 1):
        ans += (b[i] - 1) // k + 1
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(n+1)
    if m == 0:
        print(1)
        return
    if m == n:
        print(0)
        return
    d = []
    for i in range(m):
        d.append(a[i+1] - a[i] - 1)
    d.sort()
    k = d[0]
    for i in range(m-1):
        d[i+1] -= k
        if d[i+1] < 0:
            d[i+1] = 0
    print(sum(d) // k + 1)

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    A = [0] + A + [N+1]
    B = []
    for i in range(M+1):
        if A[i+1]-A[i]-1 != 0:
            B.append(A[i+1]-A[i]-1)
    if M == 0:
        print(1)
    elif M == N:
        print(0)
    else:
        K = min(B)
        print(sum((b-1)//K+1 for b in B))

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(0)
    A.append(N+1)
    A.sort()
    #print(A)
    #print(N, M)
    if M == 0:
        print(1)
        return
    else:
        L = []
        for i in range(M+1):
            L.append(A[i+1]-A[i]-1)
        L.sort()
        #print(L)
        ans = 0
        for i in range(M+1):
            if L[i] == 0:
                continue
            else:
                ans += L[i]
        print(ans)
        return

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A + [N + 1]

    dist = []
    for i in range(M + 1):
        dist.append(A[i + 1] - A[i] - 1)

    max_dist = max(dist)
    if max_dist == 0:
        print(0)
    else:
        print(max_dist - dist.count(max_dist) + 1)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # 青色のマスの位置を取得
    blue = [0] * (N + 1)
    for i in range(M):
        blue[A[i]] = 1

    # 青色のマスの位置を取得
    blue = [0] * (N + 1)
    for i in range(M):
        blue[A[i]] = 1

    # 青色のマスの間隔を取得
    interval = []
    cnt = 0
    for i in range(1, N + 1):
        if blue[i] == 1:
            if cnt != 0:
                interval.append(cnt)
            cnt = 0
        else:
            cnt += 1
    if cnt != 0:
        interval.append(cnt)

    # 青色のマスの間隔が2以上の場合、間隔の最小値を取得
    if len(interval) == 0:
        print(0)
    elif len(interval) == 1:
        print(1)
    else:
        min_interval = min(interval)
        if min_interval == 1:
            print(2)
        else:
            print((min_interval + 1) // 2)
