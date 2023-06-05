def main():
    # 读取输入
    a = int(input())
    b = int(input())
    # 通过判断a+b的和来确定正确答案
    if a + b == 4:
        print(1)
    elif a + b == 3:
        print(2)
    else:
        print(3)

if __name__ == '__main__':
    main()