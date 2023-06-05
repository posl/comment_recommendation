def main():
    # 读入数据
    data = []
    for i in range(10):
        data.append(input())
    # 找出最左边的#和最右边的#
    left = 10
    right = 0
    for i in range(10):
        for j in range(10):
            if data[i][j] == '#':
                if j < left:
                    left = j
                if j > right:
                    right = j
    # 找出最上面的#和最下面的#
    top = 10
    bottom = 0
    for i in range(10):
        for j in range(10):
            if data[i][j] == '#':
                if i < top:
                    top = i
                if i > bottom:
                    bottom = i
    # 输出结果
    print(top+1, right+1)
    print(bottom+1, left+1)

if __name__ == '__main__':
    main()