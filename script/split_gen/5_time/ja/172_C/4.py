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
