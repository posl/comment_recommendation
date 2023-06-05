def main():
    # 读入数据
    N = int(input())
    H = list(map(int, input().split()))
    # 从右向左检查
    for i in range(N - 1, 0, -1):
        if H[i] < H[i - 1]:
            H[i - 1] -= 1
    # 输出结果
    for i in range(N - 1):
        if H[i] > H[i + 1]:
            print('No')
            break
    else:
        print('Yes')

if __name__ == '__main__':
    main()