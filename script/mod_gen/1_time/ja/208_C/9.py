def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 配列Aをソート
    A.sort()
    # 配列Bを作成
    B = [0 for _ in range(N)]
    for i in range(N):
        B[i] = A[i] - i - 1
    # print(B)
    # 配列Bの中でK以下の最大値を探す
    left = 0
    right = N - 1
    while right - left > 1:
        mid = (left + right) // 2
        if B[mid] <= K:
            left = mid
        else:
            right = mid
    # print(left, right)
    # K以下の最大値のインデックスを取得
    if B[right] <= K:
        index = right
    else:
        index = left
    # print(index)
    # お菓子の配り方
    if index == N - 1:
        # 全員に1個ずつ配る
        for i in range(N):
            print(1 + K // N)
    else:
        # K以下の最大値のインデックスの国民に1個ずつ配る
        for i in range(N):
            if i <= index:
                print(1)
            else:
                print(0)
        # K - B[index]個のお菓子を配る
        for i in range(K - B[index]):
            print(A[index] + i + 1)

if __name__ == '__main__':
    main()