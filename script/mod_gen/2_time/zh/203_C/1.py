def main():
    # 读入数据
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    # AB.sort(key=lambda x: x[0])
    # print(AB)
    # 处理数据
    AB.sort(key=lambda x: x[0])
    # print(AB)
    for i in range(N):
        if K >= AB[i][0]:
            K += AB[i][1]
        else:
            break
    # 输出结果
    print(K)

if __name__ == '__main__':
    main()