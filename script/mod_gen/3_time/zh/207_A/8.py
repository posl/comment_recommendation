def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 计算答案
    ans = max(a + b, b + c, c + a)
    # 打印答案
    print(ans)

if __name__ == '__main__':
    main()