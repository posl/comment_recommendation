def main():
    # 读取数据
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    # 计算结果
    ans = a * d - b * c
    # 输出结果
    print(ans)

if __name__ == '__main__':
    main()