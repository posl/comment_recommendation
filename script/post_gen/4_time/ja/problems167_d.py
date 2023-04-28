Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    visited = [False] * n
    visited[0] = True
    now = 0
    cnt = 0
    while True:
        now = a[now] - 1
        cnt += 1
        if visited[now]:
            break
        visited[now] = True
    k -= cnt
    k %= cnt
    for _ in range(k):
        now = a[now] - 1
    print(now + 1)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    k = k % n
    i = 0
    while i < k:
        i += 1
        a = [a[a[j]-1] for j in range(n)]
    print(a[0])

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [A[i] - 1 for i in range(N)]
    B = [-1] * N
    B[0] = 0
    now = 0
    for i in range(1, N):
        now = A[now]
        if B[now] == -1:
            B[now] = i
            continue
        loop = i - B[now]
        break
    else:
        loop = N
    now = 0
    K %= loop
    for i in range(K):
        now = A[now]
    print(now + 1)

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    keta = 0
    while k > 0:
        keta += 1
        k //= 2
    keta += 1
    #print(keta)
    keta = min(keta, 200000)
    #print(keta)
    dp = [[0 for _ in range(keta)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = a[i]-1
    for i in range(1,keta):
        for j in range(n):
            dp[j][i] = dp[dp[j][i-1]][i-1]
    #print(dp)
    ans = 0
    for i in range(keta):
        if (k >> i) & 1:
            ans = dp[ans][i]
    print(ans+1)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [-1]*n
    b[0] = 0
    c = [0]
    d = [0]
    e = 0
    while True:
        e = a[e]-1
        c.append(e)
        if b[e] != -1:
            break
        b[e] = len(c)-1
    f = b[e]
    g = len(c)-1-f
    if k < f:
        print(c[k]+1)
    else:
        k -= f
        k %= g
        print(c[f+k]+1)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    v = [0]*n
    v[0] = 1
    next = a[0]-1
    cnt = 1
    while v[next] == 0:
        v[next] = 1
        next = a[next]-1
        cnt += 1
    if k <= cnt:
        for i in range(k):
            next = a[next]-1
        print(next+1)
    else:
        k -= cnt
        k %= cnt
        for i in range(k):
            next = a[next]-1
        print(next+1)

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a = [i-1 for i in a]
    now = 0
    for i in range(61):
        if k & (1<<i):
            now = a[now]
        a = [a[a[j]] for j in range(n)]
    print(now+1)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [1]
    c = [1]
    d = [0] * n
    for i in range(n):
        b.append(a[b[-1] - 1])
        c.append(b[-1])
        if d[b[-1] - 1] == 0:
            d[b[-1] - 1] = i + 1
        else:
            break
    if k < d[b[-1] - 1]:
        print(c[k])
    else:
        print(c[d[b[-1] - 1] + (k - d[b[-1] - 1]) % (i + 1) - 1])

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    visited = [False] * (N + 1)
    visited[1] = True
    # print(visited)
    # print(A)
    # print(A[0])
    # print(visited[A[0]])
    # print(visited[A[0]] == False)
    count = 0
    ans = 1
    while count < K:
        ans = A[ans - 1]
        if visited[ans] == False:
            visited[ans] = True
            count += 1
        else:
            break
    print(ans)

=======
Suggestion 10

def get_ints(): return map(int, input().split())
