def main():
    # 读取输入
    n, k = map(int, input().split())
    # 计算结果
    ans = 0 if n % k == 0 else 1
    # 输出结果
    print(ans)

if __name__ == '__main__':
    main()