def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == "#":
                continue
            tmp = 0
            # 上
            for i in range(h, -1, -1):
                if S[i][w] == "#":
                    break
                tmp += 1
            # 下
            for i in range(h, H):
                if S[i][w] == "#":
                    break
                tmp += 1
            # 左
            for i in range(w, -1, -1):
                if S[h][i] == "#":
                    break
                tmp += 1
            # 右
            for i in range(w, W):
                if S[h][i] == "#":
                    break
                tmp += 1
            ans = max(ans, tmp)
    print(ans - 3)
