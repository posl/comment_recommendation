def main():
    # 读取数据
    N = int(input())
    # 处理数据
    result = "Yay!" if int(N * 1.08) < 206 else "so-so" if int(N * 1.08) == 206 else ":("
    # 输出结果
    print(result)

if __name__ == '__main__':
    main()