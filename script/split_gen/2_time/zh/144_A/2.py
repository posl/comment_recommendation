def main():
    # 读取输入
    # 用空格分割输入的字符串，然后转换成整数
    a, b = map(int, input().split())
    # 如果a和b都在1到9之间，那么打印a×b
    if a >= 1 and a <= 9 and b >= 1 and b <= 9:
        print(a * b)
    # 否则，打印-1
    else:
        print(-1)
main()
