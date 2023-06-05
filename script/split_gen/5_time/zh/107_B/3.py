def main():
    #print("请输入行数H和列数W：")
    H, W = map(int, input().split())
    #print("请输入网格：")
    a = [list(input()) for i in range(H)]
    #print("输入的网格为：")
    #print(a)
    #print("网格的行数为：",len(a))
    #print("网格的列数为：",len(a[0]))
    #print("网格的第一行为：")
    #print(a[0])
    #print("网格的第一列为：")
    #print([x[0] for x in a])
    row = [0]*H
    col = [0]*W
    for i in range(H):
        for j in range(W):
            if a[i][j] == "#":
                row[i] = 1
                col[j] = 1
    #print("网格的行状态为：")
    #print(row)
    #print("网格的列状态为：")
    #print(col)
    for i in range(H):
        if row[i] == 1:
            for j in range(W):
                if col[j] == 1:
                    print(a[i][j], end="")
            print()
