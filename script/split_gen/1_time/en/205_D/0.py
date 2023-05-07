def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    # print(N, Q)
    # print(A)
    # print(K)
    # 1. Aの差分を求める
    # 2. Aの差分の要素数を求める
    # 3. 差分の要素数がK以下なら、Aの最後の要素に足す
    # 4. 差分の要素数がKより大きいなら、差分の要素数の値を出力する
    # 1. Aの差分を求める
    diff = []
    for i in range(N-1):
        diff.append(A[i+1] - A[i])
    # print(diff)
    # 2. Aの差分の要素数を求める
    diff_num = []
    for i in range(N-1):
        diff_num.append(diff[i]-1)
    # print(diff_num)
    # 3. 差分の要素数がK以下なら、Aの最後の要素に足す
    # 4. 差分の要素数がKより大きいなら、差分の要素数の値を出力する
    for i in range(Q):
        if sum(diff_num) < K[i]:
            print(A[-1] + (K[i] - sum(diff_num)))
        else:
            print(diff_num[K[i]-1])
