def main():
    # 標準入力から値を取得する
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    # 一番人気のジェットコースターに乗ることができる人の数を出力
    count = 0
    for i in range(n):
        if h[i] >= k:
            count += 1
    print(count)
