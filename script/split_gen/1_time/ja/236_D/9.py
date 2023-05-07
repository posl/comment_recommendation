def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    #print(A)
    #2^N通りの2人組を作る
    #2人組の相性をBに格納
    B = []
    for i in range(2**N):
        #print(i)
        x = 0
        for j in range(N):
            if (i >> j) & 1:
                x = x ^ A[j][j+1]
        B.append(x)
    #print(B)
    #2人組の相性をビットごとに見ていく
    #2人組の相性のビットごとの排他的論理和を求める
    #最大値を出力
    ans = 0
    for i in range(30):
        #print(i)
        x = 0
        for j in range(2**N):
            if (B[j] >> i) & 1:
                x += 1
        ans = ans + max(x, 2**N - x) * 2**i
    print(ans)
