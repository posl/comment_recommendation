def main():
    # 入力
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    # 処理
    p.sort()
    ans = sum(p[:K])
    # 出力
    print(ans)
