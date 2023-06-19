def main():
    # 读取输入
    N, A, B = map(int, input().split())
    # 构造输出
    for i in range(N * A):
        if i % A == 0:
            line = ''
        for j in range(N * B):
            if j % B == 0:
                line += '.'
            elif i % A == 0:
                line += '#'
            else:
                line += '.'
        print(line)

if __name__ == '__main__':
    main()