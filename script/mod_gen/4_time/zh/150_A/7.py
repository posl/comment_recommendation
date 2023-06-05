def main():
    # 读入输入
    k, x = map(int, input().split())
    # 根据题目逻辑，只需要判断2个数的大小即可，不需要存储K个500日元的硬币
    # 因此，不需要循环，直接判断即可
    if k * 500 >= x:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()