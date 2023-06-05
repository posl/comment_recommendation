Synthesizing 10/10 solutions

=======
Suggestion 1

def chessboard():
    h, w = map(int, input().split())
    s = [input() for i in range(h)]
    count = 0
    for i in range(h):
        count += s[i].count("#")
    print(count)

chessboard()

=======
Suggestion 2

def get_input():
    H, W = input().split()
    H = int(H)
    W = int(W)
    S = []
    for i in range(H):
        S.append(input())
    return H, W, S

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    count = 0
    for i in range(h):
        s = input()
        for j in range(w):
            if s[j] == '#':
                count += 1
    print(count)

=======
Suggestion 4

def count_chess():
    # 读取输入
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    # 计算棋子数
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                count += 1
    # 输出结果
    print(count)

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    print(sum(s[i][j] == '#' for i in range(h) for j in range(w)))
    #print(sum(s[i][j] == '#' for i in range(h) for j in range(w)))  # 用for循环的话，会超时
    #print(sum(s[i].count('#') for i in range(h)))  # 用for循环的话，会超时

=======
Suggestion 6

def main():
    # 读取输入
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # 处理
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    # 输出结果
    print(ans)

=======
Suggestion 7

def main():
    h,w = map(int,input().split())
    s = []
    for i in range(h):
        s.append(input())
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                ans += 1
    print(ans)

=======
Suggestion 8

def problems280_a():
    pass

=======
Suggestion 9

def problems280_a():
    h,w = map(int,input().split())
    ans = 0
    for i in range(h):
        s = input()
        for j in range(w):
            if s[j] == '#':
                ans += 1
    print(ans)

=======
Suggestion 10

def main():
    # 读取输入
    h, w = map(int, input().split())
    # 用列表保存输入的字符串
    s = []
    for i in range(h):
        s.append(input())

    # 计数器
    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                count += 1
    print(count)

main()
