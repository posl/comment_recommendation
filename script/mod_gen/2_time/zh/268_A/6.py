def main():
    # 读取输入
    nums = input().split()
    # 去重
    nums = set(nums)
    # 打印输出
    print(len(nums))

if __name__ == '__main__':
    main()