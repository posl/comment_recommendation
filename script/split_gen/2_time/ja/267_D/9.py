def main():
    #入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #処理
    # 累積和
    B = [0]
    for i in range(N):
        B.append(B[i] + A[i])
    #print(B)
    # 1つ目の部分列
    ans = 0
    for i in range(1, M+1):
        ans += i * A[i-1]
    #print(ans)
    # 2つ目の部分列以降
    for i in range(2, N-M+2):
        tmp = 0
        for j in range(1, M+1):
            tmp += j * A[i+j-2]
        #print(tmp)
        ans = max(ans, tmp)
    #出力
    print(ans)
