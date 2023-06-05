def main():
    # 读取输入
    x = input().split(" ")
    # print(x)
    # print(type(x))
    for i in range(0, 5):
        if x[i] == "0":
            print(i + 1)
            break

if __name__ == '__main__':
    main()