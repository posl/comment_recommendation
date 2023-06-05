def main():
    # 读取数据
    N, M = map(int, input().split())
    s_c = []
    for i in range(M):
        s_c.append(list(map(int, input().split())))
    # 从小到大排序
    s_c.sort()
    # 从最大的数开始，逐个减1，直到满足条件
    num = ''
    for i in range(10 ** N - 1, -1, -1):
        num = str(i)
        flag = True
        for j in range(M):
            if num[s_c[j][0] - 1] != str(s_c[j][1]):
                flag = False
                break
        if flag:
            break
    # 输出结果
    if flag:
        print(num)
    else:
        print(-1)

if __name__ == '__main__':
    main()