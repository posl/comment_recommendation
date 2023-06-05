def main():
    # 读入数据
    n = int(input())
    queries = []
    for _ in range(n):
        queries.append(list(map(int, input().split())))
    # 处理
    bag = []
    for i in range(n):
        if queries[i][0] == 1:
            bag.append(queries[i][1])
        elif queries[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += queries[i][1]
        elif queries[i][0] == 3:
            print(min(bag))
            bag.remove(min(bag))

if __name__ == '__main__':
    main()