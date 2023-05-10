def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                # 右方向
                cnt = 0
                k = j
                while k < W:
                    if S[i][k] == "#":
                        break
                    else:
                        cnt += 1
                    k += 1
                # 左方向
                k = j
                while k >= 0:
                    if S[i][k] == "#":
                        break
                    else:
                        cnt += 1
                    k -= 1
                # 上方向
                k = i
                while k >= 0:
                    if S[k][j] == "#":
                        break
                    else:
                        cnt += 1
                    k -= 1
                # 下方向
                k = i
                while k < H:
                    if S[k][j] == "#":
                        break
                    else:
                        cnt += 1
                    k += 1
                ans = max(ans, cnt-3)
    print(ans)
main()
