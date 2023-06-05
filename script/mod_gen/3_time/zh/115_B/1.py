def main():
    # 读取数据
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    # 处理
    p.sort()
    p[-1] = p[-1] / 2
    # 输出结果
    print(int(sum(p)))

if __name__ == '__main__':
    main()