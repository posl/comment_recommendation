def main():
    N = int(input())
    A = list(map(int, input().split()))
    # ボールの数をカウント
    cnt = [0] * N
    for i in range(N):
        cnt[A[i] - 1] += 1
    # 答えを計算
    ans = [0] * N
    for i in range(N):
        ans[i] = N * (N - 1) // 2 - (cnt[A[i] - 1] - 1)
    # 答えを出力
    for i in range(N):
        print(ans[i])
