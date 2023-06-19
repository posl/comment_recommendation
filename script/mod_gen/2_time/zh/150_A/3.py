def main():
    # 读取输入
    k, x = map(int, input().split())
    # 处理
    if k * 500 >= x:
        print('是')
    else:
        print('否')

if __name__ == '__main__':
    main()