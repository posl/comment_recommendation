def main():
    # 将输入的五个整数存入列表
    a = list(map(int, input().split()))
    # 将列表转换为集合，集合中的元素不重复
    b = set(a)
    # 打印集合的长度
    print(len(b))

if __name__ == '__main__':
    main()