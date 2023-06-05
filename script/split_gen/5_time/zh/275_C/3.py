def main():
    # 读取输入
    S = []
    for i in range(9):
        S.append(input())
    # 计算
    count = 0
    for r in range(9):
        for c in range(9):
            if S[r][c] == "#":
                if r+1 < 9 and c+1 < 9 and S[r+1][c] == "#" and S[r][c+1] == "#" and S[r+1][c+1] == "#":
                    count += 1
    print(count)
