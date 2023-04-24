Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2 ** K):
        tmp = [0] * N
        for j in range(K):
            if (i >> j) & 1:
                tmp[CD[j][1] - 1] += 1
            else:
                tmp[CD[j][0] - 1] += 1
        cnt = 0
        for j in range(M):
            if tmp[AB[j][0] - 1] > 0 and tmp[AB[j][1] - 1] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2**K):
        D = [0] * (N + 1)
        for j in range(K):
            if (i >> j) & 1:
                D[CD[j][1]] += 1
            else:
                D[CD[j][0]] += 1
        cnt = 0
        for j in range(M):
            if D[AB[j][0]] > 0 and D[AB[j][1]] > 0:
                cnt += 1
        ans = max(ans, cnt)
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
        cnt = [0] * N
        for j in range(K):
            if (i >> j) & 1:
                cnt[CD[j][1]-1] += 1
            else:
                cnt[CD[j][0]-1] += 1
        ans = max(ans, sum([1 for a, b in AB if cnt[a-1] > 0 and cnt[b-1] > 0]))
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2 ** K):
        d = [0] * (N + 1)
        for j in range(K):
            if (i >> j) & 1:
                d[CD[j][1]] += 1
            else:
                d[CD[j][0]] += 1
        cnt = 0
        for a, b in AB:
            if d[a] >= 1 and d[b] >= 1:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [tuple(map(int, input().split())) for _ in range(K)]

    ans = 0
    for i in range(1 << K):
        dish = [0] * (N + 1)
        for j in range(K):
            if (i >> j) & 1:
                dish[CD[j][1]] += 1
            else:
                dish[CD[j][0]] += 1
        cnt = 0
        for a, b in AB:
            if dish[a] > 0 and dish[b] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    K = int(input())
    C = [0] * K
    D = [0] * K
    for i in range(K):
        C[i], D[i] = map(int, input().split())
    ans = 0
    for i in range(2 ** K):
        cnt = 0
        dish = [0] * N
        for j in range(K):
            if i & (1 << j):
                dish[C[j] - 1] += 1
            else:
                dish[D[j] - 1] += 1
        for j in range(M):
            if dish[A[j] - 1] > 0 and dish[B[j] - 1] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2**K):
        dish = [0] * N
        for j in range(K):
            if (i >> j) & 1:
                dish[CD[j][0]-1] += 1
            else:
                dish[CD[j][1]-1] += 1
        cnt = 0
        for j in range(M):
            if dish[AB[j][0]-1] > 0 and dish[AB[j][1]-1] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 8

def main():
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
    for i in range(2**K):
        cnt = 0
        dish = [0] * (N+1)
        for j in range(K):
            if ((i >> j) & 1):
                dish[C[j]] += 1
            else:
                dish[D[j]] += 1
        for j in range(M):
            if dish[A[j]] > 0 and dish[B[j]] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 9

def main():
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
    for i in range(2**K):
        cnt = [0]*(N+1)
        for j in range(K):
            if (i>>j)&1:
                cnt[C[j]] += 1
            else:
                cnt[D[j]] += 1
        tmp = 0
        for j in range(M):
            if cnt[A[j]] > 0 and cnt[B[j]] > 0:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    K = int(input())
    C = [0]*K
    D = [0]*K
    for i in range(K):
        C[i], D[i] = map(int, input().split())
    ans = 0
    for i in range(1 << K):
        dish = [0]*N
        for j in range(K):
            if ((i >> j) & 1):
                dish[C[j]-1] += 1
            else:
                dish[D[j]-1] += 1
        cnt = 0
        for j in range(M):
            if dish[A[j]-1] > 0 and dish[B[j]-1] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
