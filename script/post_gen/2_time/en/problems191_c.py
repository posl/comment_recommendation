Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                if i != 0 and S[i - 1][j] == '.':
                    ans += 1
                if i != H - 1 and S[i + 1][j] == '.':
                    ans += 1
                if j != 0 and S[i][j - 1] == '.':
                    ans += 1
                if j != W - 1 and S[i][j + 1] == '.':
                    ans += 1
    print(ans)

main()

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                if i == 0 or i == h-1 or j == 0 or j == w-1:
                    ans = 2
                else:
                    ans = 4
    print(ans)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(1, H-1):
        for j in range(1, W-1):
            if S[i][j] == '#':
                ans = 4
                if S[i-1][j] == '#':
                    ans -= 1
                if S[i+1][j] == '#':
                    ans -= 1
                if S[i][j-1] == '#':
                    ans -= 1
                if S[i][j+1] == '#':
                    ans -= 1
    print(ans)

main()

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    S = []
    for _ in range(H):
        S.append(input())
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                ans += 1
    print(ans)

=======
Suggestion 6

def get_input():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    return h, w, s

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    #print(S)
    #print(H, W)
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])
    #print(S[4])
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
    #print(S[5][1])
    #print(S[5][2])
    #print(S[5][3])

    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                print(i, j)
                #print(S[i][j])
                #print(S[i-1][j])
                #print(S[i+1][j])
                #print(S[i

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    #print(S)

    #外枠を白に塗りつぶす
    for i in range(H):
        S[i][0] = '.'
        S[i][W-1] = '.'
    for j in range(W):
        S[0][j] = '.'
        S[H-1][j] = '.'

    #print(S)
    #白のマスを見つける
    white = []
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                white.append((i, j))

    #print(white)
    #白マスから黒マスにたどり着くまでを探索する
    for i, j in white:
        #print(i, j)
        if i-1 >= 0 and S[i-1][j] == '#':
            print(4)
            return
        if i+1 < H and S[i+1][j] == '#':
            print(4)
            return
        if j-1 >= 0 and S[i][j-1] == '#':
            print(4)
            return
        if j+1 < W and S[i][j+1] == '#':
            print(4)
            return

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    # まず、白の部分を塗りつぶす
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                S[i][j] = 'x'

    # 左上から右下への経路を見つける
    # まず、左上から右に行き、下に行く
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if j == 0:
                if S[i-1][j] == '#':
                    S[i][j] = '#'
                continue
            if S[i][j-1] == '#':
                S[i][j] = '#'
    # 次に、左下から上に行き、右に行く
    for i in range(H-1, -1, -1):
        for j in range(W-1, -1, -1):
            if i == H-1 and j == W-1:
                continue
            if i == H-1:
                if S[i][j+1] == '#':
                    S[i][j] = '#'
                continue
            if j == W-1:
                if S[i+1][j] == '#':
                    S[i][j] = '#'
                continue
            if S[i][j+1] == '#':
                S[i][j] = '#'
            if S[i+1][j] == '#':
                S[i][j] = '#'

    # まず、左上から右下への経路を見つける
    # まず、左上から右に行き、下に行く
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if j == 0:
                if S[i-1][j] == '#':
                    S[i][j] = '#'
                continue
            if S[i][j-1] == '#':
                S[i][j] = '#

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # print(S)
    # print(H, W)
    # print(S)

    # 4辺のうち、1辺でも#があれば、その辺は黒色で塗られている
    # なので、その辺の端の2点を通る直線で囲まれた部分は、黒色で塗られている
    # つまり、黒色で塗られている部分は、4辺のうち、1辺でも#があるところの部分
    # つまり、黒色で塗られている部分は、4辺のうち、1辺でも#があるところの部分
    # つまり、黒色で塗られている部分は、4辺のうち、1辺でも#があるところの部分
    # つまり、黒色で塗られている部分は、4辺のうち、1辺でも#があるところの部分
    # つまり、黒色で塗られている部分は、4辺のうち、1辺でも#があるところの部分
    # つまり、黒色で塗られている部分は、4辺のうち、1辺でも#があるところの部分
    # つまり、黒色で塗られている部分は、4辺のうち、1辺でも#があるところの部分
    # つまり、黒色で塗られている部分は、4辺のうち、1辺でも#があるところの部分
    # つまり、黒色で塗られている部分は、4辺
