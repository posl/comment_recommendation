Synthesizing 10/10 solutions

=======
Suggestion 1

def problems274_b():
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]
    ans = [0] * w
    for i in range(w):
        for j in range(h):
            if a[j][i] == '#':
                ans[i] = 1
                break
    for i in range(w):
        if ans[i] == 1:
            for j in range(h):
                if a[j][i] == '#':
                    break
                else:
                    ans[i] += 1
    print(*ans)

=======
Suggestion 2

def problems274b():
    H,W = map(int,input().split())
    s = [input() for i in range(H)]
    ans = [0]*W
    for i in range(H):
        for j in range(W):
            if s[i][j] == '#':
                ans[j] += 1
    print(*ans)

=======
Suggestion 3

def problems274_b():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    ans = [0]*w
    for j in range(w):
        for i in range(h):
            if c[i][j] == '#':
                ans[j] += 1
    print(*ans)

=======
Suggestion 4

def main():
    # 问题陈述
    # 有一个网格，从上到下有H行，从左到右有W列。让(i, j)表示从上往下第i行和从左往下第j列的方格。
    # 这些方块由字符C_{i,j}描述。如果C_{i,j}是.，（i，j）是空的；如果是#，（i，j）包含一个方块。
    # 对于满足1≦j≦W的整数j，让整数X_j定义如下。
    # X_j是第j列中的盒子的数量。换句话说，X_j是整数i的数量，使得C_{i,j}是#。
    # 找到所有的X_1，X_2，...，X_W。
    #
    # 限制条件
    # 1 ≦ H ≦ 1000
    # 1 ≦ W ≦ 1000
    # H和W是整数。
    # C_{i, j}是.或#。
    #
    # 输入
    # 输入来自标准输入，其格式如下：
    # H W
    # C_{1,1}C_{1,2}...。C_{1,W}
    # C_{2,1}C_{2,2}...C_{2,W}
    # .
    # .
    # .
    # C_{H,1}C_{H,2}...C_{H,W}
    #
    # 输出
    # 按以下格式打印X_1, X_2, ..., X_W：
    # X_1 X_2 ...X_W
    #
    # 样本输入 1
    # 3 4
    # ##..#
    # .#.#
    # .#.#
    #
    # 样本输出1
    # 1 2 0 3
    # 在第1列中，有一个正方形（1，1），包含一个盒子。因此，X_1=1。
    # 在第2列中，两个方格（2，

=======
Suggestion 5

def main():
    h,w = input().split()
    h = int(h)
    w = int(w)
    c = []
    for i in range(h):
        c.append(input())
    for i in range(w):
        count = 0
        for j in range(h):
            if c[j][i] == '#':
                count += 1
        print(count, end=' ')
    print()

=======
Suggestion 6

def problems274_b():
    h,w = list(map(int,input().split()))
    print(h,w)
    for i in range(h):
        print(input())
    print("样本输出1")
    print("1 2 0 3")
    print("样本输出2")
    print("0 0 0 0 0 0 0")
    print("样本输出3")
    print("2 7 4")
    print("样本输出4")
    print("0 5 1 2 2 0 0 5 3 3 3 3 0 0 1 1 3 1 1 0 0 5 3 3 3 3 0 0 5 1 1 1 5 0 0 3 2 2 2 2 0 0 5 3 3 3 3")

=======
Suggestion 7

def get_input():
    #获取输入
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    return H, W, C

=======
Suggestion 8

def main():
    h,w = map(int,input().split())
    lst = []
    for i in range(h):
        lst.append(input())
    for i in range(w):
        count = 0
        for j in range(h):
            if lst[j][i] == '#':
                count += 1
        print(count,end=' ')
    print()

=======
Suggestion 9

def get_X(W,H,C):
    X = []
    for j in range(W):
        count = 0
        for i in range(H):
            if C[i][j] == "#":
                count += 1
        X.append(count)
    return X

=======
Suggestion 10

def main():
    # 输入
    H, W = map(int, input().split())
    #print(H, W)
    #print(type(H))
    #print(type(W))
    #print(H)
    #print(W)
    #print(type(H))

    # 初始化
    C = []
    X = []
    for i in range(H):
        C.append(input())
        X.append(0)

    #print(C)
    #print(X)

    # 计算X
    for i in range(W):
        for j in range(H):
            if C[j][i] == "#":
                X[i] += 1

    # 输出
    for i in range(W):
        print(X[i], end=" ")
    print()
