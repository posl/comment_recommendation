def main():
    # 入力
    N = int(input())
    # 処理
    i = 1
    cnt = 0
    while i * i <= N:
        j = 1
        while i * j <= N:
            cnt += 1
            j += 1
        i += 1
    # 出力
    print(cnt)
