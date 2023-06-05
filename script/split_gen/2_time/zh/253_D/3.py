def main():
    # 读取输入
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    # 问题求解
    S = []
    for i in range(Q):
        if query[i][0] == 1:
            S.append(query[i][1])
        elif query[i][0] == 2:
            for j in range(min(query[i][2], S.count(query[i][1]))):
                S.remove(query[i][1])
        else:
            print(max(S) - min(S))
