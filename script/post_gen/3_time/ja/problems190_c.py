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
        dish = [0] * (N + 1)
        for j in range(K):
            if (i >> j) & 1:
                dish[CD[j][0]] += 1
            else:
                dish[CD[j][1]] += 1
        tmp = 0
        for j in range(M):
            if dish[AB[j][0]] > 0 and dish[AB[j][1]] > 0:
                tmp += 1
        ans = max(ans, tmp)

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
        balls = [0] * (N + 1)
        for j in range(K):
            if (i >> j) & 1:
                balls[CD[j][0]] += 1
            else:
                balls[CD[j][1]] += 1
        cnt = 0
        for j in range(M):
            if balls[AB[j][0]] >= 1 and balls[AB[j][1]] >= 1:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    cd = [list(map(int, input().split())) for _ in range(k)]

    ans = 0
    for i in range(2 ** k):
        dish = [0] * (n + 1)
        for j in range(k):
            if (i >> j) & 1:
                dish[cd[j][0]] += 1
            else:
                dish[cd[j][1]] += 1
        cnt = 0
        for a, b in ab:
            if dish[a] > 0 and dish[b] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

main()

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [tuple(map(int, input().split())) for _ in range(K)]

    ans = 0
    for i in range(2**K):
        balls = [0] * N
        for j in range(K):
            if (i>>j) & 1:
                balls[CD[j][0]-1] += 1
            else:
                balls[CD[j][1]-1] += 1
        cnt = 0
        for ab in AB:
            if balls[ab[0]-1] >= 1 and balls[ab[1]-1] >= 1:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for i in range(K)]
    ans = 0
    for i in range(2**K):
        dish = [0] * (N+1)
        for j in range(K):
            if ((i >> j) & 1):
                dish[CD[j][0]] += 1
            else:
                dish[CD[j][1]] += 1
        count = 0
        for j in range(M):
            if dish[AB[j][0]] > 0 and dish[AB[j][1]] > 0:
                count += 1
        ans = max(ans, count)
    print(ans)

=======
Suggestion 6

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
    for i in range(2**K):
        balls = [0] * N
        for j in range(K):
            if ((i >> j) & 1):
                balls[C[j]-1] += 1
            else:
                balls[D[j]-1] += 1
        cnt = 0
        for j in range(M):
            if balls[A[j]-1] > 0 and balls[B[j]-1] > 0:
                cnt += 1
        ans = max(ans, cnt)

    print(ans)

=======
Suggestion 7

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
        ball = [0]*N
        for j in range(K):
            if ((i>>j)&1):
                ball[CD[j][0]-1] += 1
            else:
                ball[CD[j][1]-1] += 1
        tmp = 0
        for j in range(M):
            if ball[AB[j][0]-1] > 0 and ball[AB[j][1]-1] > 0:
                tmp += 1
        ans = max(ans,tmp)
    print(ans)

=======
Suggestion 8

def func():
    N, M = map(int, input().split())
    AB = []
    for i in range(M):
        AB.append(list(map(int, input().split())))
    K = int(input())
    CD = []
    for i in range(K):
        CD.append(list(map(int, input().split())))

    ans = 0
    for i in range(2**K):
        dish = [0] * (N+1)
        for j in range(K):
            if ((i >> j) & 1):
                dish[CD[j][0]] += 1
            else:
                dish[CD[j][1]] += 1
        cnt = 0
        for i in range(M):
            if dish[AB[i][0]] > 0 and dish[AB[i][1]] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 9

def main():
    # 標準入力受け取り
    N,M = map(int,input().split())
    AB = []
    for _ in range(M):
        AB.append(list(map(int,input().split())))
    K = int(input())
    CD = []
    for _ in range(K):
        CD.append(list(map(int,input().split())))

    # bit全探索
    ans = 0
    for i in range(2**K):
        # 皿ごとにボールの数を格納するリスト
        dish = [0] * (N+1)
        # 人ごとにボールを置く皿を決める
        for j in range(K):
            # 人jが皿Cjにボールを置く場合
            if (i>>j)&1:
                dish[CD[j][0]] += 1
            # 人jが皿Djにボールを置く場合
            else:
                dish[CD[j][1]] += 1
        # 条件の数をカウント
        cnt = 0
        for j in range(M):
            if dish[AB[j][0]] > 0 and dish[AB[j][1]] > 0:
                cnt += 1
        ans = max(ans,cnt)
    print(ans)

=======
Suggestion 10

def check(s, N, M, AB, K, CD):
    ans = 0
    for i in range(M):
        if s[AB[i][0]-1] and s[AB[i][1]-1]:
            ans += 1
    return ans

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [list(map(int, input().split())) for _ in range(K)]

ans = 0
for i in range(2**K):
    s = [0]*N
    for j in range(K):
        if (i>>j)&1:
            s[CD[j][0]-1] = 1
        else:
            s[CD[j][1]-1] = 1
    ans = max(ans, check(s, N, M, AB, K, CD))
print(ans)
