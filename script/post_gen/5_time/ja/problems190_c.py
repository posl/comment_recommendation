Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]

    ans = 0
    for i in range(2**K):
        dish = [0] * (N+1)
        for j in range(K):
            if (i >> j) & 1:
                dish[CD[j][0]] += 1
            else:
                dish[CD[j][1]] += 1
        cnt = 0
        for a, b in AB:
            if dish[a] > 0 and dish[b] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for i in range(K)]
    ans = 0
    for i in range(2**K):
        cnt = [0]*N
        for j in range(K):
            if i>>j&1:
                cnt[CD[j][0]-1] += 1
            else:
                cnt[CD[j][1]-1] += 1
        tmp = 0
        for j in range(M):
            if cnt[AB[j][0]-1] > 0 and cnt[AB[j][1]-1] > 0:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]

    ans = 0
    for i in range(2**K):
        dish = [0 for _ in range(N+1)]
        for j in range(K):
            if (i>>j)&1:
                dish[CD[j][0]] += 1
            else:
                dish[CD[j][1]] += 1

        cnt = 0
        for k in range(M):
            if dish[AB[k][0]] > 0 and dish[AB[k][1]] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    K = int(input())
    C = []
    D = []
    for i in range(K):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)

    ans = 0
    for i in range(2 ** K):
        balls = [0] * (N + 1)
        for j in range(K):
            if ((i >> j) & 1):
                balls[C[j]] += 1
            else:
                balls[D[j]] += 1

        now = 0
        for j in range(M):
            if balls[A[j]] > 0 and balls[B[j]] > 0:
                now += 1
        ans = max(ans, now)
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    c = [list(map(int, input().split())) for _ in range(k)]

    ans = 0
    for i in range(2 ** k):
        dish = [0] * (n + 1)
        for j in range(k):
            if (i >> j) & 1:
                dish[c[j][0]] += 1
            else:
                dish[c[j][1]] += 1
        tmp = 0
        for a_i, b_i in a:
            if dish[a_i] >= 1 and dish[b_i] >= 1:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = [0 for _ in range(m)]
    b = [0 for _ in range(m)]
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    k = int(input())
    c = [0 for _ in range(k)]
    d = [0 for _ in range(k)]
    for i in range(k):
        c[i], d[i] = map(int, input().split())
    ans = 0
    for i in range(2 ** k):
        dish = [0 for _ in range(n)]
        for j in range(k):
            if (i >> j) & 1:
                dish[d[j] - 1] += 1
            else:
                dish[c[j] - 1] += 1
        cnt = 0
        for j in range(m):
            if dish[a[j] - 1] > 0 and dish[b[j] - 1] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]

    ans = 0
    for i in range(2 ** K):
        dish = [0] * (N + 1)
        for j in range(K):
            if (i >> j) & 1:
                dish[CD[j][1]] += 1
            else:
                dish[CD[j][0]] += 1

        cnt = 0
        for k in range(M):
            if dish[AB[k][0]] > 0 and dish[AB[k][1]] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0

    for i in range(2**K):
        dish = [0] * (N+1)
        for j in range(K):
            if ((i >> j) & 1):
                dish[CD[j][0]] += 1
            else:
                dish[CD[j][1]] += 1
        cnt = 0
        for j in range(M):
            if dish[AB[j][0]] != 0 and dish[AB[j][1]] != 0:
                cnt += 1
        if ans < cnt:
            ans = cnt
    print(ans)

=======
Suggestion 9

def main():
    n,m = list(map(int, input().split()))
    ab = []
    for i in range(m):
        ab.append(list(map(int, input().split())))
    k = int(input())
    cd = []
    for i in range(k):
        cd.append(list(map(int, input().split())))
    ans = 0
    for i in range(2**k):
        tmp = [0]*n
        for j in range(k):
            if ((i>>j)&1):
                tmp[cd[j][0]-1] += 1
            else:
                tmp[cd[j][1]-1] += 1
        cnt = 0
        for j in range(m):
            if tmp[ab[j][0]-1] and tmp[ab[j][1]-1]:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [tuple(map(int, input().split())) for _ in range(K)]

    ans = 0
    for i in range(2**K):
        cnt = [0]*N
        for j in range(K):
            if (i>>j)&1:
                cnt[CD[j][0]-1] += 1
            else:
                cnt[CD[j][1]-1] += 1
        tmp = 0
        for a, b in AB:
            if cnt[a-1] and cnt[b-1]:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)
