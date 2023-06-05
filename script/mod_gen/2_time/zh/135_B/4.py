def main():
    # 读取输入
    a, b = map(int, input().split())
    # 判断输出
    if (a+b)%2 != 0:
        print("IMPOSSIBLE")
    else:
        print((a+b)//2)

if __name__ == '__main__':
    main()