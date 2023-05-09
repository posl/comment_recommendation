def main():
    #入力
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    #マス (X, Y) から見えるマスの数を求める
    count = 1
    #上下左右に障害物がない限り計算
    for i in range(1, max(H, W)):
        #上
        if X - i - 1 >= 0:
            if S[X - i - 1][Y - 1] == ".":
                count += 1
            else:
                break
        #下
        if X + i - 1 < H:
            if S[X + i - 1][Y - 1] == ".":
                count += 1
            else:
                break
        #左
        if Y - i - 1 >= 0:
            if S[X - 1][Y - i - 1] == ".":
                count += 1
            else:
                break
        #右
        if Y + i - 1 < W:
            if S[X - 1][Y + i - 1] == ".":
                count += 1
            else:
                break
    #出力
    print(count)
