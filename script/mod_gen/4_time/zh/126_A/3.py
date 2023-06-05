def main():
    # 读取输入
    n, k = map(int, input().split())
    s = input()
    # 解决方案
    print(s[:k-1] + s[k-1].lower() + s[k:])

if __name__ == '__main__':
    main()