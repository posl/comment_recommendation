def main():
    # 读入数据
    Q = int(input())
    # 用字典存储数据
    A = {}
    # 用列表存储查询
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    # 处理查询
    for i in range(Q):
        if query[i][0] == 1:
            h = query[i][1]
            while A.get(h % 1048576) != None:
                h += 1
            A[h % 1048576] = query[i][1]
        else:
            print(A.get(query[i][1] % 1048576))
