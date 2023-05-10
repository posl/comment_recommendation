def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                tmp = 0
                for k in range(j+1, W):
                    if S[i][k] == '.':
                        tmp += 1
                    else:
                        break
                for k in range(j-1, -1, -1):
                    if S[i][k] == '.':
                        tmp += 1
                    else:
                        break
                for k in range(i+1, H):
                    if S[k][j] == '.':
                        tmp += 1
                    else:
                        break
                for k in range(i-1, -1, -1):
                    if S[k][j] == '.':
                        tmp += 1
                    else:
                        break
                ans = max(ans, tmp+1)
    print(ans)
