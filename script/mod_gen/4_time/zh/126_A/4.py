def main():
    # 1. 获取输入
    n, k = map(int, input().split())
    s = input()
    # 2. 处理
    result = s[:k-1] + s[k-1].lower() + s[k:]
    # 3. 输出
    print(result)

if __name__ == '__main__':
    main()