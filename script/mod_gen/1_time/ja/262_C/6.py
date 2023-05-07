def main():
    N = int(input())
    A = list(map(int, input().split()))
    # Aの各要素の個数をカウントする
    cnt = [0] * (N + 1)
    for i in range(N):
        cnt[A[i]] += 1
    # Aの各要素の個数の累積和を計算する
    sum_cnt = [0] * (N + 1)
    for i in range(N):
        sum_cnt[i + 1] = sum_cnt[i] + cnt[i + 1]
    # Aの各要素の個数の累積和を用いて、
    # min(A[i], A[j]) = i, max(A[i], A[j]) = j を満たす
    # (i, j) の個数を求める
    ans = 0
    for i in range(N):
        # A[i] = i の場合
        if A[i] == i + 1:
            ans += sum_cnt[N] - sum_cnt[i + 1]
        # A[i] > i の場合
        elif A[i] > i + 1:
            ans += cnt[A[i]]
    print(ans)

if __name__ == '__main__':
    main()