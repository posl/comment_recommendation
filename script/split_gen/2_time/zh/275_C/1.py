def main():
    # 读取输入
    S = []
    for i in range(9):
        S.append(input())
    # 统计
    count = 0
    for r in range(9):
        for c in range(9):
            if S[r][c] == "#":
                count += 1
    # 输出
    print(count)
