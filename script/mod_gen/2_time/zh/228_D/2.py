def main():
    # 读入输入
    q = int(input())
    query = []
    for i in range(q):
        query.append(list(map(int, input().split())))
    # 用于存储结果
    result = []
    # 用于存储序列A
    A = [-1 for i in range(2 ** 20)]
    # 处理查询
    for i in range(q):
        if query[i][0] == 1:
            h = query[i][1]
            while A[h % (2 ** 20)] != -1:
                h += 1
            A[h % (2 ** 20)] = query[i][1]
        else:
            result.append(A[query[i][1] % (2 ** 20)])
    # 输出结果
    for i in range(len(result)):
        print(result[i])

if __name__ == '__main__':
    main()