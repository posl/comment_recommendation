def main():
    # 读取输入
    A, B = map(int, input().split())
    # 计算答案
    ans = 32 ** (A - B)
    # 利用print()函数输出结果
    print(ans)

if __name__ == '__main__':
    main()