def main():
    # 1行目の入力を取得
    n = int(input())
    # 2行目の入力を取得
    s = input()
    # 3行目の入力を取得
    w = list(map(int, input().split()))
    # f(x)を求める
    def f(x):
        cnt = 0
        for i in range(n):
            if s[i] == '0':
                if w[i] < x:
                    cnt += 1
            else:
                if w[i] >= x:
                    cnt += 1
        return cnt
    # Xを動かす範囲を定義
    left = 0
    right = 10 ** 9 + 1
    # 二分探索
    while right - left > 1:
        mid = (left + right) // 2
        if f(mid) == n:
            left = mid
        else:
            right = mid
    # 答えを出力
    print(left)
