def main():
    # 读取数据
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    # 统计票数
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    # 找出最多票数
    max = 0
    for i in d:
        if d[i] > max:
            max = d[i]
    # 打印最多票数的字符串
    for i in sorted(d):
        if d[i] == max:
            print(i)

if __name__ == '__main__':
    main()