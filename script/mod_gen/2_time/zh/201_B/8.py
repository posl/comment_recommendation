def main():
    # 读入数据
    N = int(input())
    ST = []
    for i in range(N):
        ST.append(input().split())
    # 由于ST中的第二个元素是字符串，所以需要转换成数字才能进行排序
    for i in range(N):
        ST[i][1] = int(ST[i][1])
    # 按照山的高度排序
    ST.sort(key=lambda x: x[1], reverse=True)
    # 打印第二高的山的名字
    print(ST[1][0])

if __name__ == '__main__':
    main()