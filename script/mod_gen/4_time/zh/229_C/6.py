def main():
    # 读取数据
    n, w = map(int, input().split())
    cheese = []
    for i in range(n):
        cheese.append(list(map(int, input().split())))
    # 从小到大排序
    cheese.sort(key=lambda x: x[0]/x[1])
    # 计算总和
    total = 0
    for i in cheese:
        if w >= i[1]:
            total += i[0]
            w -= i[1]
        else:
            total += i[0] * (w / i[1])
            break
    print(int(total))

if __name__ == '__main__':
    main()