def main():
    # 入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 処理
    ans = 0
    for i in range(N-M+1):
        ans = max(ans, sum(A[i:i+M]) + sum(range(1, M+1)))
    # 出力
    print(ans)
