def main():
    # 读入输入
    n = int(input())
    a = list(map(int, input().split()))
    # 排序
    a.sort()
    # 打印答案
    print(a[1])

if __name__ == '__main__':
    main()