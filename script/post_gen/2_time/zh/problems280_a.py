Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    h,w = map(int, input().split())
    s = [input() for i in range(h)]
    return h,w,s

=======
Suggestion 2

def main():
    # 读取输入
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # 计算答案
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    # 打印输出
    print(ans)

main()

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    s = [input() for i in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                count += 1
    print(count)

=======
Suggestion 4

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
Suggestion 5

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    print(sum([s.count('#') for s in S]))

=======
Suggestion 6

def get_input():
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    return h, w, s

=======
Suggestion 7

def main():
    #输入
    h,w = map(int,input().split())
    s = []
    for i in range(h):
        s.append(input())
    #计算
    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                count += 1
    #输出
    print(count)

=======
Suggestion 8

def main():
    h,w = map(int,input().split())
    grid = [[c for c in input()] for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#':
                count += 1
    print(count)

=======
Suggestion 9

def problems280_a():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    print(ans)

problems280_a()

=======
Suggestion 10

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                ans += 1
    print(ans)
