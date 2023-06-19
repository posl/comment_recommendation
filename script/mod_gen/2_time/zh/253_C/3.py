def main():
    # 读取输入
    n = int(input())
    queries = []
    for i in range(n):
        queries.append(input().split())
    # print(queries)
    # 处理
    s = []
    for i in range(n):
        if queries[i][0] == '1':
            s.append(int(queries[i][1]))
        elif queries[i][0] == '2':
            num = int(queries[i][1])
            count = int(queries[i][2])
            for j in range(count):
                s.remove(num)
        elif queries[i][0] == '3':
            s.sort()
            print(s[-1] - s[0])
        else:
            pass

if __name__ == '__main__':
    main()