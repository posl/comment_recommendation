Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    print(S)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    #print(H, W)
    #print(S)

    #マス目の左上、左下、右上、右下の隅をそれぞれ (0, 0), (H, 0), (0, W), (H, W) とする座標系で表す
    #左上から右上、右上から右下、右下から左下、左下から左上の順で頂点を見る
    #黒マスを見つけたらそのマスの左上、左下、右上、右下の隅をそれぞれ (0, 0), (H, 0), (0, W), (H, W) とする座標系で表す
    #上記の順で頂点を見ていく
    #黒マスを見つけたらそのマスの左上、左下、右上、右下の隅をそれぞれ (0, 0), (H, 0), (0, W), (H, W) とする座標系で表す
    #上記の順で頂点を見ていく
    #黒マスを見つけたらそのマスの左上、左下、右上、右下の隅をそれぞれ (0, 0), (H, 0), (0, W), (H, W) とする座標系で表す
    #上記の順で頂点を見ていく
    #黒マスを見つけたらそのマスの左上、左下、右上、右下の隅をそれぞれ (0, 0), (H, 0), (0, W), (H, W) とする座標系で表す
    #上記の順で頂点を見ていく
    #黒マスを見つけたらそのマスの左上

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    print(min(H, W))

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    S = [[0 for _ in range(W)] if s == '.' else [1 for _ in range(W)] for s in S]
    #print(S)
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])
    #print(S[4])
    #print(S[5])
    #print(S[6])
    #print(S[7])
    #print(S[8])
    #print(S[9])
    #print(S[10])
    #print(S[11])
    #print(S[12])
    #print(S[13])
    #print(S[14])
    #print(S[15])
    #print(S[16])
    #print(S[17])
    #print(S[18])
    #print(S[19])
    #print(S[20])
    #print(S[21])
    #print(S[22])
    #print(S[23])
    #print(S[24])
    #print(S[25])
    #print(S[26])
    #print(S[27])
    #print(S[28])
    #print(S[29])
    #print(S[30])
    #print(S[31])
    #print(S[32])
    #print(S[33])
    #print(S[34])
    #print(S[35])
    #print(S[36])
    #print(S[37])
    #print(S[38])
    #print(S[39])
    #print(S[40])
    #print(S[41])
    #print(S[42])
    #print(S[43])
    #print(S[44])
    #print(S[45])
    #print(S[46])
    #print(S[47])
    #print(S[48])
    #print(S[49])
    #print(S[50])
    #print(S[51])
    #print(S[52])
    #print(S[53])
    #print(S[54])
    #print(S[55])
    #print(S[56])
    #print(S[57])
    #print(S[58])
    #print(S[59])
    #print(S[60])
    #print(S[61])
    #print(S[62

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    #print(S)
    #print(H, W)
    #print(S[0][0])
    
    #左上から黒マスを探す
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                #print(i, j)
                break
        if S[i][j] == '#':
            break
    
    #print(i, j)
    
    #左上から黒マスを探す
    for k in range(H):
        for l in range(W):
            if S[H-k-1][W-l-1] == '#':
                #print(i, j)
                break
        if S[H-k-1][W-l-1] == '#':
            break
    
    #print(H-k-1, W-l-1)
    
    #左上から黒マスを探す
    for m in range(H):
        for n in range(W):
            if S[m][W-n-1] == '#':
                #print(i, j)
                break
        if S[m][W-n-1] == '#':
            break
    
    #print(m, W-n-1)
    
    #左上から黒マスを探す
    for o in range(H):
        for p in range(W):
            if S[H-o-1][p] == '#':
                #print(i, j)
                break
        if S[H-o-1][p] == '#':
            break
    
    #print(H-o-1, p)
    
    #print(i, j, H-k-1, W-l-1, m, W-n-1, H-o-1, p)
    
    #print(i, j, H-k-1, W-l-1, m, W-n-1, H-o-1, p)
    #if i == H-k-1 and j == W-l-1:
    #    print(1)
    #elif i == H-k-1 and j == W-n-1:
    #    print(1)
    #elif i == H-o-1 and j == W-l-1:
    #    print(1)

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    s = [list(input()) for _ in range(H)]
    #print(s)
    #print(s[0])
    #print(s[0][1])
    #print(s[0][3])
    #print(s[0][4])
    #print(s[0][5])
    #print(s[1][1])
    #print(s[2][1])
    #print(s[3][1])
    #print(s[4][1])
    #print(s[4][3])
    #print(s[4][4])
    #print(s[4][5])
    #print(s[3][3])
    #print(s[2][3])
    #print(s[1][3])
    #print(s[1][4])
    #print(s[1][5])
    #print(s[2][5])
    #print(s[3][5])
    #print(s[4][5])
    #print(s[4][4])
    #print(s[4][3])
    #print(s[4][2])
    #print(s[4][1])
    #print(s[3][1])
    #print(s[2][1])
    #print(s[1][1])
    #print(s[1][2])
    #print(s[1][3])
    #print(s[1][4])
    #print(s[1][5])
    #print(s[2][5])
    #print(s[3][5])
    #print(s[4][5])
    #print(s[4][4])
    #print(s[4][3])
    #print(s[4][2])
    #print(s[4][1])
    #print(s[3][1])
    #print(s[2][1])
    #print(s[1][1])
    #print(s[1][2])
    #print(s[1][3])
    #print(s[1][4])
    #print(s[1][5])
    #print(s[2][5])
    #print(s[3][5])
    #print(s[4][5])
    #print(s[4][4])
    #print(s[4][3])
    #print(s[4][2])
    #print(s[4][1])
    #

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    #print(S)
    #print(H, W)
    #print(S[0][0])
    #print(S[0][1])
    #print(S[0][2])
    #print(S[0][3])
    #print(S[0][4])
    #print(S[1][0])
    #print(S[1][1])
    #print(S[1][2])
    #print(S[1][3])
    #print(S[1][4])
    #print(S[2][0])
    #print(S[2][1])
    #print(S[2][2])
    #print(S[2][3])
    #print(S[2][4])
    #print(S[3][0])
    #print(S[3][1])
    #print(S[3][2])
    #print(S[3][3])
    #print(S[3][4])
    #print(S[4][0])
    #print(S[4][1])
    #print(S[4][2])
    #print(S[4][3])
    #print(S[4][4])
    
    #print(S[0][0])
    #print(S[1][0])
    #print(S[2][0])
    #print(S[3][0])
    #print(S[4][0])
    
    #print(S[0][4])
    #print(S[1][4])
    #print(S[2][4])
    #print(S[3][4])
    #print(S[4][4])
    
    #print(S[0][0])
    #print(S[0][1])
    #print(S[0][2])
    #print(S[0][3])
    #print(S[0][4])
    
    #print(S[4][0])
    #print(S[4][1])
    #print(S[4][2])
    #print(S[4][3])
    #print(S[4][4])
    
    #print(S[1][1])
    #print(S[1][2])
    #print(S[1][3])
    
    #print(S[2][1])
    #print(S[2][2])
    #print(S[

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    #print(S)
    #print(H, W)
    #print(S[0][0])
    #print(S[1][1])
    #print(S[2][2])
    #print(S[3][3])
    #print(S[4][4])
    #print(S[0][1])
    #print(S[0][2])
    #print(S[0][3])
    #print(S[0][4])
    #print(S[1][0])
    #print(S[2][0])
    #print(S[3][0])
    #print(S[4][0])
    #print(S[1][2])
    #print(S[1][3])
    #print(S[1][4])
    #print(S[2][1])
    #print(S[3][1])
    #print(S[4][1])
    #print(S[2][3])
    #print(S[2][4])
    #print(S[3][2])
    #print(S[4][2])
    #print(S[3][4])
    #print(S[4][3])
    #print(S[4][4])
    #print(S[0][0])
    #print(S[1][1])
    #print(S[2][2])
    #print(S[3][3])
    #print(S[4][4])
    #print(S[0][1])
    #print(S[0][2])
    #print(S[0][3])
    #print(S[0][4])
    #print(S[1][0])
    #print(S[2][0])
    #print(S[3][0])
    #print(S[4][0])
    #print(S[1][2])
    #print(S[1][3])
    #print(S[1][4])
    #print(S[2][1])
    #print(S[3][1])
    #print(S[4][1])
    #print(S[2][3])
    #print(S[2][4])
    #print(S[3][2])
    #print(S[4][2])
    #print(S[3][4])
    #print(S[4][3])
    #

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    #print(S)
    #print(H,W)
    #print(S[0][0])
    #print(S[0][W-1])
    #print(S[H-1][0])
    #print(S[H-1][W-1])
    #print(S[1][1])
    #print(S[1][2])
    #print(S[1][3])
    #print(S[2][1])
    #print(S[2][2])
    #print(S[2][3])
    #print(S[3][1])
    #print(S[3][2])
    #print(S[3][3])
    #print(S[4][1])
    #print(S[4][2])
    #print(S[4][3])
    #print(S[1][1])
    #print(S[2][1])
    #print(S[3][1])
    #print(S[4][1])
    #print(S[1][2])
    #print(S[2][2])
    #print(S[3][2])
    #print(S[4][2])
    #print(S[1][3])
    #print(S[2][3])
    #print(S[3][3])
    #print(S[4][3])
    #print(S[1][4])
    #print(S[2][4])
    #print(S[3][4])
    #print(S[4][4])
    #print(S[1][5])
    #print(S[2][5])
    #print(S[3][5])
    #print(S[4][5])
    #print(S[1][6])
    #print(S[2][6])
    #print(S[3][6])
    #print(S[4][6])
    #print(S[1][7])
    #print(S[2][7])
    #print(S[3][7])
    #print(S[4][7])
    #print(S[1][8])
    #print(S[2][8])
    #print(S[3][8])
    #print(S[4][8])
    #print(S[1][9])
    #print(S[2][9])
    #print(S[3
