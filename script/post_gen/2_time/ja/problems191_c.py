Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    print(solve(H, W, S))

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    #print(S)
    n = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                n += 1
    print(n)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    #print(S)
    #print(S[0])
    #print(S[0][0])
    #print(S[0][1])

    #print(S[0][0] == "#")
    #print(S[0][1] == "#")

    #print(S[0][0] == ".")

    #print(S[0][0] == "." and S[0][1] == "#")
    #print(S[0][0] == "#" and S[0][1] == ".")

    #print(S[0][0] == "." and S[0][1] == "#" and S[1][0] == "#")
    #print(S[0][0] == "." and S[0][1] == "#" and S[1][0] == ".")

    #print(S[0][0] == "." and S[0][1] == "#" and S[1][0] == "." and S[1][1] == "#")
    #print(S[0][0] == "." and S[0][1] == "#" and S[1][0] == "." and S[1][1] == ".")

    #print(S[0][0] == "." and S[0][1] == "#" and S[1][0] == "." and S[1][1] == "." and S[1][2] == "#")
    #print(S[0][0] == "." and S[0][1] == "#" and S[1][0] == "." and S[1][1] == "." and S[1][2] == ".")

    #print(S[0][0] == "." and S[0][1] == "#" and S[1][0] == "." and S[1][1] == "." and S[1][2] == "." and S[2][0] == "#")
    #print(S[0][0] == "." and S[0][1] == "#" and S[1][0] == "." and S[1][1] == "." and S[1][2] == "." and S[2][0] == ".")

    #print(S[0][0] == "." and S[

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    #print(S)
    #print(H, W)
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
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
    #print(S[0][0] == '#')
    #print(S[0][1] == '#')
    #print(S[0][2] == '#')
    #print(S[0][3] == '#')
    #print(S[0][4] == '#')
    #print(S[1][0] == '#')
    #print(S[1][1] == '#')
    #print(S[1][2] == '#')
    #print(S[1][3] == '#')
    #print(S[1][4] == '#')
    #print(S[2][0] == '#')
    #print(S[2][1] == '#')
    #print(S[2][2] == '#')
    #print(S[2][3] == '#')
    #print(S[2][4] == '#')
    #print(S[3][0] == '#')
    #print(S[3][1] ==

=======
Suggestion 6

def main():
    H, W = list(map(int, input().split()))
    S = [list(map(str, input())) for _ in range(H)]
    #print(S)
    #print(S[0][0])
    #print(S[0][1])
    #print(S[1][0])
    #print(S[1][1])
    #print(S[2][0])
    #print(S[2][1])
    #print(S[0][0] == '#')
    #print(S[0][1] == '#')
    #print(S[1][0] == '#')
    #print(S[1][1] == '#')
    #print(S[2][0] == '#')
    #print(S[2][1] == '#')
    #print(S[0][0] == '.' and S[0][1] == '.' and S[1][0] == '.' and S[1][1] == '.')
    #print(S[0][0] == '.' and S[0][1] == '.' and S[1][0] == '.' and S[1][1] == '.' and S[2][0] == '.' and S[2][1] == '.')
    #print(S[0][0] == '#' and S[0][1] == '#' and S[1][0] == '#' and S[1][1] == '#')
    #print(S[0][0] == '#' and S[0][1] == '#' and S[1][0] == '#' and S[1][1] == '#' and S[2][0] == '#' and S[2][1] == '#')
    #print(S[0][0] == '#' and S[0][1] == '.' and S[1][0] == '#' and S[1][1] == '.')
    #print(S[0][0] == '.' and S[0][1] == '#' and S[1][0] == '.' and S[1][1] == '#')
    #print(S[0][0] == '#' and S[0][1] == '.' and S[1][0] == '.' and S[1][1] == '#')
    #print(S[0][0] == '.' and S[0][1] == '#' and S[1][0] == '#'

=======
Suggestion 7

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

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    #print(S)
    #print(H, W)

    # H, W = 5, 5
    # S = [['.', '.', '.', '.', '.'], ['.', '#', '#', '#', '.'], ['.', '#', '#', '#', '.'], ['.', '#', '#', '#', '.'], ['.', '.', '.', '.', '.']]

    # H, W = 5, 6
    # S = [['.', '.', '.', '.', '.', '.'], ['.', '#', '#', '#', '#', '.'], ['.', '#', '#', '#', '#', '.'], ['.', '#', '#', '#', '#', '.'], ['.', '.', '.', '.', '.', '.']]

    # H, W = 6, 5
    # S

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    #print(S)

    #左から探索
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                left = j
                break
        if S[i][j] == "#":
            break

    #右から探索
    for i in range(H):
        for j in range(W-1, -1, -1):
            if S[i][j] == "#":
                right = j
                break
        if S[i][j] == "#":
            break

    #上から探索
    for i in range(W):
        for j in range(H):
            if S[j][i] == "#":
                up = j
                break
        if S[j][i] == "#":
            break

    #下から探索
    for i in range(W):
        for j in range(H-1, -1, -1):
            if S[j][i] == "#":
                down = j
                break
        if S[j][i] == "#":
            break

    #print(left, right, up, down)
    print(right-left+down-up+4)

=======
Suggestion 10

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
