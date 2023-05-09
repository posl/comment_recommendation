def main():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]
    #print(S)
    #黒マスを白マスに変換
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                S[i] = S[i][:j] + '.' + S[i][j+1:]
    #print(S)
    #白マスを黒マスに変換
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                S[i] = S[i][:j] + '#' + S[i][j+1:]
    #print(S)
    #上下左右のマスを調べる
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                if S[i-1][j] == '.':
                    count += 1
                if S[i+1][j] == '.':
                    count += 1
                if S[i][j-1] == '.':
                    count += 1
                if S[i][j+1] == '.':
                    count += 1
    print(count//2)

if __name__ == '__main__':
    main()