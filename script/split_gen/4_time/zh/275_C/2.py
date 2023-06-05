def main():
    # 读取输入
    input = []
    for i in range(9):
        input.append(input())
    # 遍历每个点，检查是否有四个顶点都有棋子的正方形
    count = 0
    for r in range(9):
        for c in range(9):
            if input[r][c] == "#":
                if r + 1 < 9 and c + 1 < 9 and input[r + 1][c] == "#" and input[r][c + 1] == "#" and input[r + 1][
                    c + 1] == "#":
                    count += 1
    print(count)
