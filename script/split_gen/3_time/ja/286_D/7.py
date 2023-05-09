def main():
    # 入力
    N, X = map(int, input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    # 1枚も使わない場合を追加
    A.append(0)
    B.append(0)
    # 計算
    ans = "No"
    for i in range(N+1):
        for j in range(N+1):
            if A[i]*i + A[j]*j == X:
                ans = "Yes"
    # 出力
    print(ans)
