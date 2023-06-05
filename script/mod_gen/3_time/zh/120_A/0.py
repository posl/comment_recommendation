def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 处理
    if a * c <= b:
        ans = c
    else:
        ans = b // a
    # 输出结果
    print(ans)

if __name__ == '__main__':
    main()