Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N,M = map(int,input().split())
    AB = []
    for i in range(M):
        AB.append(list(map(int,input().split())))
    K = int(input())
    CD = []
    for i in range(K):
        CD.append(list(map(int,input().split())))
    ans = 0
    for i in range(2**K):
        cnt = 0
        balls = [0]*N
        for j in range(K):
            if (i>>j)&1:
                balls[CD[j][0]-1] += 1
            else:
                balls[CD[j][1]-1] += 1
        for k in range(M):
            if balls[AB[k][0]-1] and balls[AB[k][1]-1]:
                cnt += 1
        ans = max(ans,cnt)
    print(ans)

=======
Suggestion 2

def main():
    # 读取标准输入
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
    # 求解
    ans = 0
    for i in range(2**K):
        dish = [0] * N
        for j in range(K):
            if ((i >> j) & 1):
                dish[C[j] - 1] += 1
            else:
                dish[D[j] - 1] += 1
        cnt = 0
        for j in range(M):
            if dish[A[j] - 1] >= 1 and dish[B[j] - 1] >= 1:
                cnt += 1
        ans = max(ans, cnt)
    # 打印输出
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [tuple(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2 ** K):
        balls = [0] * N
        for j in range(K):
            if (i >> j) & 1:
                balls[CD[j][0] - 1] += 1
            else:
                balls[CD[j][1] - 1] += 1
        cnt = 0
        for a, b in AB:
            if balls[a - 1] and balls[b - 1]:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]

    ans = 0
    for i in range(2**K):
        balls = [0] * N
        for j in range(K):
            if (i >> j) & 1:
                balls[CD[j][0]-1] += 1
            else:
                balls[CD[j][1]-1] += 1
        cnt = 0
        for a, b in AB:
            if balls[a-1] >= 1 and balls[b-1] >= 1:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a-1)
        B.append(b-1)
    K = int(input())
    C = []
    D = []
    for _ in range(K):
        c, d = map(int, input().split())
        C.append(c-1)
        D.append(d-1)
    ans = 0
    for i in range(2 ** K):
        dish = [0] * N
        for j in range(K):
            if i >> j & 1:
                dish[C[j]] += 1
            else:
                dish[D[j]] += 1
        cnt = 0
        for j in range(M):
            if dish[A[j]] > 0 and dish[B[j]] > 0:
                cnt += 1
        if ans < cnt:
            ans = cnt
    print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    CD = [list(map(int, input().split())) for _ in range(k)]
    ans = 0
    for i in range(2 ** k):
        balls = [0] * (n + 1)
        for j in range(k):
            if i >> j & 1:
                balls[CD[j][0]] += 1
            else:
                balls[CD[j][1]] += 1
        cnt = 0
        for a, b in AB:
            if balls[a] and balls[b]:
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
        balls = [0] * (N+1)
        for j in range(K):
            if (i >> j) & 1:
                balls[CD[j][0]] += 1
            else:
                balls[CD[j][1]] += 1
        cnt = 0
        for j in range(M):
            if balls[AB[j][0]] != 0 and balls[AB[j][1]] != 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for i in range(K)]

    ans = 0
    for i in range(2**K):
        bits = [0]*K
        for j in range(K):
            if ((i>>j) & 1):
                bits[j] = 1

        balls = [0] * N
        for j in range(K):
            if bits[j] == 0:
                balls[CD[j][0]-1] += 1
            else:
                balls[CD[j][1]-1] += 1

        cnt = 0
        for j in range(M):
            if balls[AB[j][0]-1] >= 1 and balls[AB[j][1]-1] >= 1:
                cnt += 1

        if ans < cnt:
            ans = cnt

    print(ans)
