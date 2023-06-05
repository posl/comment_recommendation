def main():
    # 读入数据
    a, b, c = map(int, input().split())
    # 计算答案
    ans = a + b + c - min(a, b, c)
    # 打印答案
    print(ans)

if __name__ == '__main__':
    main()