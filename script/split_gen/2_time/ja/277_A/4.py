def main():
    # 入力
    n, x = map(int, input().split())
    p = list(map(int, input().split()))
    # 処理
    for i in range(n):
        if p[i] == x:
            ans = i + 1
    # 出力
    print(ans)
