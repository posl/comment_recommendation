def main():
    # 读取输入
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # 排序
    a.sort(reverse=True)
    # 计算总票数
    total = sum(a)
    # 判断是否为受欢迎的项目
    if a[m-1] >= total / (4 * m):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()