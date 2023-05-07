def main():
    # 入力
    N = int(input())
    d = list(map(int, input().split()))
    # 出力
    ans = 0
    for i in range(0, N):
        for j in range(i + 1, N):
            ans += d[i] * d[j]
    print(ans)
