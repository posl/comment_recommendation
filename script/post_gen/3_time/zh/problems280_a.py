Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                count += 1
    print(count)

=======
Suggestion 3

def problems280_a():
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    cnt = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    s = [input() for i in range(h)]
    print(sum([s[i].count("#") for i in range(h)]))

=======
Suggestion 5

def main():
    h = 0
    w = 0
    while True:
        try:
            h, w = map(int, input().split())
            break
        except:
            print("输入错误")
    count = 0
    for i in range(h):
        s = input()
        for j in range(len(s)):
            if s[j] == "#":
                count += 1
    print(count)

=======
Suggestion 6

def get_chess_num():
    h, w = map(int, input().split())
    chess_num = 0
    for i in range(h):
        s = input()
        for j in range(w):
            if s[j] == '#':
                chess_num += 1
    return chess_num

=======
Suggestion 7

def main():
    h,w = map(int,input().split())
    count = 0
    for i in range(h):
        count += input().count('#')
    print(count)

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                count += 1
    print(count)

=======
Suggestion 10

def main():
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    cnt = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                cnt += 1
    print(cnt)
