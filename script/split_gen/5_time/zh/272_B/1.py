def main():
    # 读入数据
    N, M = map(int, input().split())
    # 生成参加聚会的人的列表
    party = []
    for i in range(M):
        party.append(list(map(int, input().split()))[1:])
    # 生成关系矩阵
    relation = [[0] * N for i in range(N)]
    for i in range(M):
        for j in range(len(party[i])):
            for k in range(j + 1, len(party[i])):
                relation[party[i][j] - 1][party[i][k] - 1] = 1
                relation[party[i][k] - 1][party[i][j] - 1] = 1
    # 检查关系矩阵
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if relation[i][j] == 0:
                print("No")
                return
    print("Yes")
