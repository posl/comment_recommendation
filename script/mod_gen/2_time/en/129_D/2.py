def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            for k in range(4):
                cnt = 1
                while True:
                    if k == 0:
                        if i - cnt < 0 or S[i - cnt][j] == '#':
                            break
                        cnt += 1
                    elif k == 1:
                        if i + cnt > H - 1 or S[i + cnt][j] == '#':
                            break
                        cnt += 1
                    elif k == 2:
                        if j - cnt < 0 or S[i][j - cnt] == '#':
                            break
                        cnt += 1
                    elif k == 3:
                        if j + cnt > W - 1 or S[i][j + cnt] == '#':
                            break
                        cnt += 1
                ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()