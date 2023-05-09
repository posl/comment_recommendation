def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '#':
                continue
            # 上下左右の候補を作成
            cand = [(h, w)]
            for i in range(1, max(H, W)):
                if h - i >= 0:
                    cand.append((h - i, w))
                if h + i < H:
                    cand.append((h + i, w))
                if w - i >= 0:
                    cand.append((h, w - i))
                if w + i < W:
                    cand.append((h, w + i))
            # 候補の中から、#があるものを除外
            cand = list(filter(lambda x: S[x[0]][x[1]] != '#', cand))
            # 候補が多い方を採用
            if len(cand) > ans:
                ans = len(cand)
    print(ans)
