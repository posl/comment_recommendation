def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        #print(S[i])
        for j in range(W):
            if S[i][j] == '#':
                continue
            for k in range(i+1, H):
                if S[k][j] == '#':
                    break
                S[k] = S[k][:j] + '#' + S[k][j+1:]
                #print(S[k])
            for k in range(i-1, -1, -1):
                if S[k][j] == '#':
                    break
                S[k] = S[k][:j] + '#' + S[k][j+1:]
                #print(S[k])
            for k in range(j+1, W):
                if S[i][k] == '#':
                    break
                S[i] = S[i][:k] + '#' + S[i][k+1:]
                #print(S[i])
            for k in range(j-1, -1, -1):
                if S[i][k] == '#':
                    break
                S[i] = S[i][:k] + '#' + S[i][k+1:]
                #print(S[i])
    for i in range(H):
        ans += S[i].count('.')
    print(ans)
