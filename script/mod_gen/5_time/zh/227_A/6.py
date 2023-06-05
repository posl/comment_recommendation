def main():
    # 读取输入
    n, k, a = map(int, input().split())
    # print(n, k, a)
    print((k - a) % n)

if __name__ == '__main__':
    main()