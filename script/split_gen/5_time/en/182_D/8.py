def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 1. 累積和を求める
    # 2. 累積和の最大値を求める
    # 3. 1 + 2 の最大値を求める
    # 4. 3 の最大値を求める
    # 5. 4 の最大値を出力する
    B = []
    tmp = 0
    for i in range(N):
        tmp += A[i]
        B.append(tmp)
    print(max(B))
