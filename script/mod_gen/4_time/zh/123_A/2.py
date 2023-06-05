def main():
    # 读取输入
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    # 求出最大的距离
    max_distance = e - a
    # 输出结果
    if max_distance <= k:
        print("Yay!")
    else:
        print(":(")

if __name__ == '__main__':
    main()