def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                # 上下左右に道があるか確認
                if i > 0 and S[i-1][j] == '.':
                    ans += 1
                if i < H-1 and S[i+1][j] == '.':
                    ans += 1
                if j > 0 and S[i][j-1] == '.':
                    ans += 1
                if j < W-1 and S[i][j+1] == '.':
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()