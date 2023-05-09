def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    # 0 を含む区間の最大値
    max_sum = 0
    # 0 以外の区間の最大値
    max_sum2 = 0
    # 0 を含む区間の最小値
    min_sum = 0
    # 0 以外の区間の最小値
    min_sum2 = 0
    # 区間の最大値、最小値を求める
    for i in range(N):
        max_sum += max(L, A[i])
        min_sum += min(R, A[i])
        if A[i] != 0:
            max_sum2 += max(L, A[i])
            min_sum2 += min(R, A[i])
    # 0 を含む区間の最大値と最小値の差
    diff = max_sum - min_sum
    # 0 以外の区間の最大値と最小値の差
    diff2 = max_sum2 - min_sum2
    # 0 を含む区間の最大値と最小値の差が 0 でない場合
    if diff != 0:
        # 0 以外の区間の最大値と最小値の差を 0 にする
        # 最大値と最小値の差の絶対値を 2 で割った値を、
        # 0 以外の区間の最大値と最小値の差に足す
        # 0 以外の区間の最大値と最小値の差が 0 になる
        ans = max_sum2 - min_sum2 + abs(diff) // 2
    # 0 を含む区間の最大値と最小値の差が 0 の場合
    else:
        # 0 以外の区間の最大値と最

if __name__ == '__main__':
    main()