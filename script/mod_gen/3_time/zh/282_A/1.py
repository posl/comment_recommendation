def main():
    # 读取数据
    k = int(input())
    # 处理数据
    # 输出结果
    print("".join([chr(ord('A')+i) for i in range(k)]))

if __name__ == '__main__':
    main()