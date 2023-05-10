Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,M,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    sum_A = [0]
    sum_B = [0]
    for i in range(N):
        sum_A.append(sum_A[i]+A[i])
    for i in range(M):
        sum_B.append(sum_B[i]+B[i])
    ans = 0
    for i in range(N+1):
        if sum_A[i] > K:
            break
        tmp = i
        for j in range(M+1):
            if sum_A[i] + sum_B[j] > K:
                break
            tmp = i + j
        ans = max(ans,tmp)
    print(ans)

=======
Suggestion 2

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_sum = [0] * (N + 1)
    B_sum = [0] * (M + 1)
    for i in range(N):
        A_sum[i + 1] = A_sum[i] + A[i]
    for i in range(M):
        B_sum[i + 1] = B_sum[i] + B[i]
    ans = 0
    j = M
    for i in range(N + 1):
        if A_sum[i] > K:
            break
        while A_sum[i] + B_sum[j] > K:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

=======
Suggestion 3

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 机Aと机Bのそれぞれの累積和を計算
    A_cumsum = [0] * (N + 1)
    B_cumsum = [0] * (M + 1)
    for i in range(N):
        A_cumsum[i + 1] = A_cumsum[i] + A[i]
    for i in range(M):
        B_cumsum[i + 1] = B_cumsum[i] + B[i]

    # 机Bの累積和から読むことができる本の冊数の最大値を計算
    ans = 0
    for i in range(M + 1):
        if B_cumsum[i] > K:
            break
        # 机Aから読むことができる本の冊数を二分探索で計算
        ok = 0
        ng = N + 1
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if A_cumsum[mid] + B_cumsum[i] <= K:
                ok = mid
            else:
                ng = mid
        ans = max(ans, i + ok)

    print(ans)

=======
Suggestion 4

def main():
    N,M,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    sumA = [0]
    sumB = [0]
    for i in range(N):
        sumA.append(sumA[i]+A[i])
    for i in range(M):
        sumB.append(sumB[i]+B[i])
    ans = 0
    j = M
    for i in range(N+1):
        if sumA[i] > K:
            break
        while sumB[j] > K - sumA[i]:
            j -= 1
        ans = max(ans,i+j)
    print(ans)

=======
Suggestion 5

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 累積和を取る
    A_acc = [0] * (N + 1)
    for i in range(N):
        A_acc[i + 1] = A_acc[i] + A[i]
    B_acc = [0] * (M + 1)
    for i in range(M):
        B_acc[i + 1] = B_acc[i] + B[i]

    # 答えの候補を全探索
    ans = 0
    for i in range(N + 1):
        if A_acc[i] > K:
            break
        # 机 A から i 冊読む
        rest = K - A_acc[i]
        # 机 B から何冊読めるか
        cnt = bisect.bisect_right(B_acc, rest)
        ans = max(ans, i + cnt - 1)
    print(ans)

=======
Suggestion 6

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 机Aの本を読む時間の累積和
    a_sum = [0]
    for i in range(n):
        a_sum.append(a_sum[i] + a[i])

    # 机Bの本を読む時間の累積和
    b_sum = [0]
    for i in range(m):
        b_sum.append(b_sum[i] + b[i])

    ans = 0
    j = m
    for i in range(n + 1):
        if a_sum[i] > k:
            break
        while b_sum[j] > k - a_sum[i]:
            j -= 1
        ans = max(ans, i + j)

    print(ans)

=======
Suggestion 7

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 累積和
    for i in range(N - 1):
        A[i + 1] += A[i]
    for i in range(M - 1):
        B[i + 1] += B[i]

    # 机 A から i 冊、机 B から j 冊本を読んだときの合計所要時間の最大値を求める
    ans = 0
    j = M
    for i in range(N + 1):
        if A[i - 1] > K:
            break
        while B[j - 1] > K - A[i - 1]:
            j -= 1
        ans = max(ans, i + j - 1)
    print(ans)

=======
Suggestion 8

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A_sum = [0]
    B_sum = [0]
    for i in range(N):
        A_sum.append(A_sum[i] + A[i])
    for i in range(M):
        B_sum.append(B_sum[i] + B[i])

    ans = 0
    j = M
    for i in range(N+1):
        if A_sum[i] > K:
            break
        while B_sum[j] > K - A_sum[i]:
            j -= 1
        ans = max(ans, i + j)

    print(ans)

=======
Suggestion 9

def solve():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = [0]
    b = [0]
    for i in range(N):
        a.append(a[i] + A[i])
    for i in range(M):
        b.append(b[i] + B[i])
    ans = 0
    j = M
    for i in range(N + 1):
        if a[i] > K:
            break
        while b[j] > K - a[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

=======
Suggestion 10

def solve():
    # 入力
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 机Aで読むことができる本の冊数、所要時間
    a = 0
    t = 0
    for i in range(N):
        if t + A[i] <= K:
            a += 1
            t += A[i]
        else:
            break
    # 机Bで読むことができる本の冊数、所要時間
    b = 0
    t = 0
    for i in range(M):
        if t + B[i] <= K:
            b += 1
            t += B[i]
        else:
            break
    # 机Aと机Bのそれぞれで読むことができる本の冊数の合計の最大値を求める
    ans = a + b
    # 机Aの上からi冊目までの本を読んだ時の所要時間
    t = 0
    for i in range(N):
        # 机Aの上からi冊目までの本を読んだ時の所要時間
        t += A[i]
        # 机Bで読むことができる本の冊数
        b = 0
        for j in range(M):
            # 机Bの上からj冊目までの本を読んだ時の所要時間
            t += B[j]
            # 机Bで読むことができる本の冊数
            if t > K:
                break
            b += 1
        # 机Aと机Bのそれぞれで読むことができる本の冊数の合計の最大値を更新する
        ans = max(ans, i + 1 + b)
    print(ans)
