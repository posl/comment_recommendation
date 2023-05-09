def main():
    # 入力
    N = int(input())
    d = list(map(int, input().split()))
    # 処理
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += d[i] * d[j]
    # 出力
    print(ans)
