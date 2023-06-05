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
