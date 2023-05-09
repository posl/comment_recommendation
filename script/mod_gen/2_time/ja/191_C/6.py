def main():
    H, W = map(int, input().split())
    S = []
    for _ in range(H):
        S.append(input())
    #print(S)
    
    #黒マスの数をカウント
    cnt = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                cnt += 1
    #print(cnt)
    
    #黒マスの数が 3 以上の場合、
    #黒マスの数を頂点数として出力
    if cnt >= 3:
        print(cnt)
    #黒マスの数が 2 の場合、
    #黒マスの数を頂点数として出力
    elif cnt == 2:
        print(cnt)
    #黒マスの数が 1 の場合、
    #黒マスの数を頂点数として出力
    elif cnt == 1:
        print(cnt)
    #黒マスの数が 0 の場合、
    #黒マスの数を頂点数として出力
    elif cnt == 0:
        print(cnt)

if __name__ == '__main__':
    main()