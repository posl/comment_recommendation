Synthesizing 9/10 solutions

=======
Suggestion 1

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
        balls = [0] * N
        for j in range(K):
            if (i >> j) & 1:
                balls[C[j] - 1] += 1
            else:
                balls[D[j] - 1] += 1
        cnt = 0
        for j in range(M):
            if balls[A[j] - 1] >= 1 and balls[B[j] - 1] >= 1:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 2

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
    for i in range(2**K):
        tmp = 0
        ball = [0] * N
        for j in range(K):
            if (i >> j) & 1:
                ball[C[j] - 1] += 1
            else:
                ball[D[j] - 1] += 1
        for j in range(M):
            if ball[A[j] - 1] > 0 and ball[B[j] - 1] > 0:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 3

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
        balls = [0] * N
        for j in range(K):
            if ((i >> j) & 1):
                balls[C[j] - 1] += 1
            else:
                balls[D[j] - 1] += 1
        cnt = 0
        for j in range(M):
            if balls[A[j] - 1] >= 1 and balls[B[j] - 1] >= 1:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 4

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
        
        cnt = 0
        for j in range(M):
            if balls[A[j]] > 0 and balls[B[j]] > 0:
                cnt += 1
        
        ans = max(ans, cnt)
    
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    K = int(input())
    C = []
    D = []
    for _ in range(K):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)

    ans = 0
    for i in range(2**K):
        balls = [0] * (N+1)
        for j in range(K):
            if ((i >> j) & 1):
                balls[C[j]] += 1
            else:
                balls[D[j]] += 1
        cnt = 0
        for k in range(M):
            if balls[A[k]] > 0 and balls[B[k]] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

main()

=======
Suggestion 6

def main():
    # 入力
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    # ボールの数を数える
    balls = [0] * N
    for c, d in CD:
        balls[c - 1] += 1
        balls[d - 1] += 1
    # 条件を満たすかどうかを調べる
    ans = 0
    for a, b in AB:
        if balls[a - 1] >= 1 and balls[b - 1] >= 1:
            ans += 1
    # 出力
    print(ans)

=======
Suggestion 7

def main():
    #入力
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

    #全探索
    ans = 0
    for i in range(2 ** K):
        #ボールの配置
        ball = [0] * N
        for j in range(K):
            if (i >> j) & 1:
                ball[C[j] - 1] += 1
            else:
                ball[D[j] - 1] += 1

        #条件の検査
        cnt = 0
        for j in range(M):
            if ball[A[j] - 1] > 0 and ball[B[j] - 1] > 0:
                cnt += 1

        #最大値の更新
        ans = max(ans, cnt)

    #出力
    print(ans)

=======
Suggestion 8

def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2**K):
        ball = [0] * (N + 1)
        for j in range(K):
            if (i >> j) & 1:
                ball[CD[j][1]] += 1
            else:
                ball[CD[j][0]] += 1
        cnt = 0
        for k in range(M):
            if ball[AB[k][0]] > 0 and ball[AB[k][1]] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    cond = []
    for i in range(M):
        cond.append(list(map(int,input().split())))
    K = int(input())
    ball = []
    for i in range(K):
        ball.append(list(map(int,input().split())))
    ans = 0
    for i in range(2**K):
        tmp = [0]*N
        for j in range(K):
            if (i>>j)&1:
                tmp[ball[j][1]-1] += 1
            else:
                tmp[ball[j][0]-1] += 1
        cnt = 0
        for j in range(M):
            if tmp[cond[j][0]-1] > 0 and tmp[cond[j][1]-1] > 0:
                cnt += 1
        ans = max(ans,cnt)
    print(ans)
