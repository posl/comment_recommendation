def main():
    # 读取输入
    c1, c2, c3 = input().split()
    # 解决问题
    if c1 == c2 == c3:
        result = 'Won'
    else:
        result = 'Lost'
    # 打印结果
    print(result)

if __name__ == '__main__':
    main()