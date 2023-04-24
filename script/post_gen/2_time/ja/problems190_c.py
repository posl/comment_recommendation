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
        balls = [0] * (N + 1)
        for j in range(K):
            if (i >> j) & 1:
                balls[CD[j][1]] += 1
            else:
                balls[CD[j][0]] += 1
        cnt = 0
        for j in range(M):
            if balls[AB[j][0]] >= 1 and balls[AB[j][1]] >= 1:
                cnt += 1
        if cnt > ans:
            ans = cnt
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0

    for i in range(1 << K):
        balls = [0] * N
        for j in range(K):
            if (i >> j) & 1:
                balls[CD[j][0] - 1] += 1
            else:
                balls[CD[j][1] - 1] += 1
        cnt = 0
        for j in range(M):
            if balls[AB[j][0] - 1] > 0 and balls[AB[j][1] - 1] > 0:
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
    for i in range(2 ** K):
        balls = [0] * N
        for j in range(K):
            if (i >> j) & 1:
                balls[CD[j][0] - 1] += 1
            else:
                balls[CD[j][1] - 1] += 1
        cnt = 0
        for j in range(M):
            if balls[AB[j][0] - 1] > 0 and balls[AB[j][1] - 1] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [tuple(map(int, input().split())) for _ in range(K)]

    # ボールを置いた皿を記録
    # 1-indexed
    balls = [0] * (N + 1)
    ans = 0

    # 全てのパターンを試す
    for i in range(2 ** K):
        # ボールを置く
        for j in range(K):
            if ((i >> j) & 1):
                balls[CD[j][0]] += 1
            else:
                balls[CD[j][1]] += 1

        # 条件を満たすか判定
        count = 0
        for a, b in AB:
            if balls[a] and balls[b]:
                count += 1

        ans = max(ans, count)

        # ボールを取り除く
        for j in range(K):
            if ((i >> j) & 1):
                balls[CD[j][0]] -= 1
            else:
                balls[CD[j][1]] -= 1

    print(ans)

=======
Suggestion 5

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
        ball = [0] * N
        for j in range(K):
            if (i >> j) & 1:
                ball[C[j] - 1] += 1
            else:
                ball[D[j] - 1] += 1
        cnt = 0
        for j in range(M):
            if ball[A[j] - 1] > 0 and ball[B[j] - 1] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for i in range(K)]
    ans = 0
    for i in range(2**K):
        balls = [0]*N
        for j in range(K):
            if (i>>j)&1:
                balls[CD[j][0]-1] += 1
            else:
                balls[CD[j][1]-1] += 1
        cnt = 0
        for k in range(M):
            if balls[AB[k][0]-1] > 0 and balls[AB[k][1]-1] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

main()

=======
Suggestion 7

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
        balls = [0] * (N+1)
        for j in range(K):
            if (i >> j) & 1:
                balls[C[j]] += 1
            else:
                balls[D[j]] += 1
        tmp = 0
        for j in range(M):
            if balls[A[j]] > 0 and balls[B[j]] > 0:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 8

def main():
    # input
    N, M = map(int, input().split())
    ABs = [[*map(int, input().split())] for _ in range(M)]
    K = int(input())
    CDs = [[*map(int, input().split())] for _ in range(K)]

    # compute
    ans = 0
    for i in range(2**K):
        balls = [0] * (N+1)
        for j in range(K):
            if (i >> j) & 1:
                balls[CDs[j][1]] += 1
            else:
                balls[CDs[j][0]] += 1
        cnt = 0
        for AB in ABs:
            if balls[AB[0]] > 0 and balls[AB[1]] > 0:
                cnt += 1
        ans = max(ans, cnt)

    # output
    print(ans)

=======
Suggestion 9

def read_ints():
    return map(int, input().split())

N, M = read_ints()
A = [0] * M
B = [0] * M
for i in range(M):
    A[i], B[i] = read_ints()

K = int(input())
C = [0] * K
D = [0] * K
for i in range(K):
    C[i], D[i] = read_ints()

ans = 0
for i in range(2**K):
    balls = [0] * N
    for j in range(K):
        if (i >> j) & 1:
            balls[C[j] - 1] += 1
        else:
            balls[D[j] - 1] += 1

    cnt = 0
    for j in range(M):
        if balls[A[j] - 1] > 0 and balls[B[j] - 1] > 0:
            cnt += 1
    ans = max(ans, cnt)

print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    #print(N, M)
    AB = [list(map(int, input().split())) for _ in range(M)]
    #print(AB)
    K = int(input())
    #print(K)
    CD = [list(map(int, input().split())) for _ in range(K)]
    #print(CD)
    ans = 0
    for i in range(2**K):
        balls = [0] * (N+1)
        for j in range(K):
            if ((i >> j) & 1):
                balls[CD[j][0]] += 1
            else:
                balls[CD[j][1]] += 1
        #print(balls)
        cnt = 0
        for k in range(M):
            if balls[AB[k][0]] > 0 and balls[AB[k][1]] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
