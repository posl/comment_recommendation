def bingo():
    # 读取输入
    a = []
    for i in range(3):
        a.append(list(map(int, input().split())))
    n = int(input())
    b = []
    for i in range(n):
        b.append(int(input()))
    # 检查是否有bingo
    bingo = False
    for i in range(3):
        for j in range(3):
            if a[i][j] in b:
                bingo = True
                break
        if bingo:
            break
    # 输出结果
    if bingo:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    bingo()