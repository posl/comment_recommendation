Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H,W = map(int,input().split())
    S = []
    for i in range(H):
        S.append(input())
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                count += 1
    print(count)

=======
Suggestion 2

def get_input():
    # 获取输入
    print("请输入H,W")
    h, w = map(int, input().split())
    print("请输入S_1, S_2, ..., S_H")
    s = []
    for i in range(h):
        s.append(input())
    return h, w, s

=======
Suggestion 3

def problems280_a():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    print(sum([s.count("#") for s in S]))

=======
Suggestion 4

def main():
    h, w = map(int,input().split())
    s = []
    for i in range(h):
        s.append(input())
    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                count += 1
    print(count)

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                cnt += 1
    print(cnt)

=======
Suggestion 7

def problems280_a():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                count += 1
    print(count)

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                count +=1
    print(count)

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    count = 0
    for i in range(H):
        count += S[i].count('#')
    print(count)

=======
Suggestion 10

def main():
    h, w = map(int, input().split())
    count = 0
    for i in range(h):
        s = input()
        for j in range(w):
            if s[j] == '#':
                count += 1
    print(count)
