Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
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
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    # H 行 W 列のマス目があり、各マスにはコマが置かれているか、何も置かれていないかのどちらかです。
    # マス目の状態は H 個の長さ W の文字列 S_1, S_2, ..., S_H によって表され、
    # S_i の j 文字目が # のとき上から i 行目かつ左から j 列目のマスにはコマが置かれていることを、
    # S_i の j 文字目が . のとき上から i 行目かつ左から j 列目のマスには何も置かれていないことを表しています。
    # マス目上のマスのうち、コマが置かれているようなものの個数を求めてください。
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                count += 1
    print(count)

=======
Suggestion 5

def main():
    H,W = map(int,input().split())
    S = [input() for i in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    H,W = map(int,input().split())
    S = [input() for i in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    cnt = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    h,w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    #入力
    H,W = map(int,input().split())
    S = []
    for i in range(H):
        S.append(input())
    #処理
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                ans += 1
    #出力
    print(ans)

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    print(sum([s.count("#") for s in S]))
