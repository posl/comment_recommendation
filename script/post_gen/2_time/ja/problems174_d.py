Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N):
        if i % 2 == 0:
            if S[i] == "W":
                ans += 1
        else:
            if S[i] == "R":
                ans += 1
    print(min(ans, N - ans))

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == "R":
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    R = S.count("R")
    W = S.count("W")
    ans = 0
    if R > W:
        for i in range(N):
            if i % 2 == 0 and S[i] == "W":
                ans += 1
    else:
        for i in range(N):
            if i % 2 == 1 and S[i] == "R":
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    c = list(input())
    ans = 0
    for i in range(N):
        if c[i] == 'R':
            ans += 1
    print(min(ans, N - ans))

=======
Suggestion 5

def main():
    N = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    print(min(r, w))

=======
Suggestion 6

def main():
    N = int(input())
    c = input()
    r = c.count("R")
    w = N - r
    print(min(r, w))

=======
Suggestion 7

def main():
    N = int(input())
    stones = input()
    white = stones.count("W")
    red = stones.count("R")
    white_stones = stones[:white]
    red_stones = stones[white:]
    print(min(white_stones.count("R"), red_stones.count("W")))

=======
Suggestion 8

def main():
    N = int(input())
    c = input()
    # Rの数
    R = c.count('R')
    # Wの数
    W = c.count('W')
    # Rの数が少ないほう
    min = R if R < W else W
    # Rの数が多いほう
    max = R if R >= W else W
    # 連続するRの数
    cnt = 0
    # 連続するRの最大数
    max_cnt = 0
    # 連続するRの最大数を求める
    for i in range(N):
        if c[i] == 'R':
            cnt += 1
        else:
            if cnt > max_cnt:
                max_cnt = cnt
            cnt = 0
    if cnt > max_cnt:
        max_cnt = cnt
    # 結果を出力
    print(min + max - max_cnt)

main()

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    # Rの個数
    cnt_R = S.count("R")
    # Rを左から数えてi番目の時、左側にあるWの個数
    cnt_W = [0] * (N+1)
    for i in range(N):
        cnt_W[i+1] = cnt_W[i] + (S[i] == "W")
    # Rを左から数えてi番目の時、右側にあるRの個数
    cnt_R2 = [0] * (N+1)
    for i in range(N):
        cnt_R2[N-i-1] = cnt_R2[N-i] + (S[N-i-1] == "R")
    # Rを左から数えてi番目の時、左側にあるWの個数 + 右側にあるRの個数
    cnt = [cnt_W[i] + cnt_R2[i] for i in range(N+1)]
    print(min(cnt))
