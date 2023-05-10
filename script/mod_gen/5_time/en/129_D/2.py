def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '.':
                tmp = 1
                for i in range(h-1, -1, -1):
                    if S[i][w] == '#':
                        break
                    tmp += 1
                for i in range(h+1, H):
                    if S[i][w] == '#':
                        break
                    tmp += 1
                for i in range(w-1, -1, -1):
                    if S[h][i] == '#':
                        break
                    tmp += 1
                for i in range(w+1, W):
                    if S[h][i] == '#':
                        break
                    tmp += 1
                ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()