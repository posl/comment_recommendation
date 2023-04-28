Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = []
    for i in range(9):
        s.append(input())
    count = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == "#":
                count += 1
    print(count)

=======
Suggestion 2

def main():
    # input
    S = [input() for _ in range(9)]

    # compute
    cnt = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == '#':
                cnt += 1
    ans = cnt - 4

    # output
    print(ans)

=======
Suggestion 3

def main():
    ans = 0
    for i in range(9):
        S = input()
        for j in range(9):
            if S[j] == '#':
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    # input
    S = []
    for _ in range(9):
        S.append(input())

    # compute
    cnt = 0
    for r in range(9):
        for c in range(9):
            if S[r][c] == '#':
                if r-1 >= 0 and c-1 >= 0 and S[r-1][c-1] == '#':
                    if r-1 >= 0 and S[r-1][c] == '#':
                        if c-1 >= 0 and S[r][c-1] == '#':
                            cnt += 1

    # output
    print(cnt)

=======
Suggestion 5

def main():
    #input
    s = []
    for i in range(9):
        s.append(input())
    #output
    count = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == "#":
                count += 1
    print(count)

=======
Suggestion 6

def main():
    #n = int(input())
    #a = list(map(int, input().split()))
    #s = input()
    #h,w = map(int, input().split())
    #a = [list(map(int, input().split())) for _ in range(h)]
    #s = [input() for _ in range(3)]
    s = [input() for _ in range(9)]
    ans = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == "#":
                ans += 1
    print(ans)
    return

=======
Suggestion 7

def solve():
    count = 0
    for i in range(9):
        s = input()
        count += s.count("#")
    print(count)

=======
Suggestion 8

def main():
    # 標準入力の受け取り
    # 9行の文字列を受け取り、リストに格納
    S = []
    for i in range(9):
        S.append(input())
    #print(S)

    # ポーンが置かれている座標のリストを作成
    p_list = []
    for i in range(9):
        for j in range(9):
            if S[i][j] == '#':
                p_list.append([i,j])
    #print(p_list)

    # 4頂点の組み合わせを全て試して、4頂点全てにポーンが置かれているかを確認
    # 4頂点全てにポーンが置かれている正方形の個数をカウント
    count = 0
    for i in range(len(p_list)):
        for j in range(i+1,len(p_list)):
            for k in range(j+1,len(p_list)):
                for l in range(k+1,len(p_list)):
                    # 4頂点の座標を取り出す
                    p1 = p_list[i]
                    p2 = p_list[j]
                    p3 = p_list[k]
                    p4 = p_list[l]
                    #print(p1,p2,p3,p4)
                    # 4頂点全てにポーンが置かれているかを確認
                    if p1[0] == p2[0] and p1[1] == p4[1] and p3[0] == p4[0] and p2[1] == p3[1]:
                        count += 1
    #print(count)

    # 答えを出力
    print(count)

=======
Suggestion 9

def check(x, y, s):
    if s[x][y] == '#':
        return True
    return False
