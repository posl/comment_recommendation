def main():
    # 读取输入
    a, b = map(int, input().split())
    # 计算结果
    ans = 0
    for i in range(a, b+1):
        ans += 1
    # 打印结果
    print(ans)
    return

if __name__ == '__main__':
    main()