def main():
    #入力
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    #初期化
    color = set()
    ans = 0
    #処理
    for i in range(N-K+1):
        for j in range(i, i+K):
            color.add(c[j])
        if len(color) > ans:
            ans = len(color)
        color.clear()
    #出力
    print(ans)
