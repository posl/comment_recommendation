Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
        return
    ans = 200000
    for i in range(1, N):
        ans = min(ans, c[:i].count('R') + c[i:].count('W'))
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    R = S.count("R")
    W = S.count("W")
    print(min(R, W))

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    S = S.replace("R","0").replace("W","1")
    S = S.replace("0","2").replace("1","0").replace("2","1")
    print(min(S.count("01"),S.count("10")))

=======
Suggestion 4

def main():
    N = int(input())
    c = input()
    R = c.count("R")
    W = c.count("W")
    print(min(R, W))

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    #print(N)
    #print(S)
    R = S.count('R')
    W = S.count('W')
    ans = 0
    if R==0 or W==0:
        ans = 0
    else:
        ans = min(R,W)
        for i in range(N):
            if S[i]=='R':
                R -= 1
            else:
                W -= 1
            ans = min(ans,R+W)
    print(ans)

=======
Suggestion 6

def input():
    return open(0).readline()

N = int(input())
S = input().strip()
ans = 0
for i in range(N):
    if S[i] == 'R':
        for j in range(i+1,N):
            if S[j] == 'W':
                ans += 1
                S = S[:i] + 'W' + S[i+1:j] + 'R' + S[j+1:]
                break
print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()

    # 左からi番目までの石のうち、赤い石の個数
    red = [0]
    for s in S:
        if s == "R":
            red.append(red[-1] + 1)
        else:
            red.append(red[-1])

    ans = 10**9
    for i in range(1, N + 1):
        # 左からi番目までの白い石のうち、左隣に赤い石がある個数
        left = red[i] - 1
        # 右からi番目までの白い石のうち、右隣に赤い石がある個数
        right = N - i - (red[-1] - red[i])
        ans = min(ans, left + right)

    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    s = input()
    #白を右端に移動させる
    s = s.replace("R", "0").replace("W", "R").replace("0", "W")
    #白を右端に移動させた後の文字列から、左から順に赤を探し、その位置をリストに格納
    red = [i for i in range(N) if s[i] == "R"]
    #赤の位置のリストから、順に右に移動させるための操作回数を計算
    ans = sum(red[i] - i for i in range(len(red)))
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    c = input()
    # 石の色の配列を作成
    c_list = []
    for i in range(N):
        c_list.append(c[i])
    #print(c_list)
    # 赤い石の左隣に置かれた白い石の数をカウント
    count = 0
    for i in range(N-1):
        if c_list[i] == 'R' and c_list[i+1] == 'W':
            count += 1
    print(count)
