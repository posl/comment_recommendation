def main():
    # 读取输入
    a, b = map(int, input().split())
    # 初始化答案
    ans = 0
    # 遍历所有的整数
    for i in range(1, 101):
        # 如果整数的范围在a和b之间
        if a <= i and i <= b:
            # 答案+1
            ans += 1
    # 输出答案
    print(ans)

if __name__ == '__main__':
    main()