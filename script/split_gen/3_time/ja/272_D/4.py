def main():
    N, M = map(int, input().split())
    # 答えを格納する配列
    ans = [[-1] * N for _ in range(N)]
    # 駒を置くマスをキューに入れる
    que = [(0, 0)]
    # キューが空になるまで繰り返す
    while len(que) > 0:
        # キューの先頭を取り出す
        i, j = que.pop(0)
        # すでに答えが出ているマスはスキップ
        if ans[i][j] >= 0:
            continue
        # 答えを出す
        ans[i][j] = int((i**2 + j**2)**0.5)
        # 4 方向のマスに駒を移動させる
        for di, dj in zip([1, 0, -1, 0], [0, 1, 0, -1]):
            ni = i + di
            nj = j + dj
            # マスが範囲外ならスキップ
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            # 答えが出ていないマスをキューに入れる
            if ans[ni][nj] < 0:
                que.append((ni, nj))
    # 答えを出力する
    for i in range(N):
        print(*ans[i])
