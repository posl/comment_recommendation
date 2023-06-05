def main():
    # 读取输入
    n, k = map(int, input().split())
    # 计算答案
    print(min(n % k, k - n % k))

if __name__ == '__main__':
    main()