def main():
    # 读取输入
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    # 求解并输出
    print(max(a-c, a-d, b-c, b-d))

if __name__ == '__main__':
    main()