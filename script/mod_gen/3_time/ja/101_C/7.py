def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # Aの最大値を求める
    max_A = max(A)
    # Aの各要素が何回変更されるかを求める
    change = [0] * (max_A + 1)
    for i in range(N):
        change[A[i]] += 1
    # 変更回数の最大値を求める
    max_change = max(change)
    # 変更回数の最大値から操作回数を求める
    print(K - max_change)

if __name__ == '__main__':
    main()