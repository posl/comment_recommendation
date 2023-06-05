def main():
    # 读取输入
    k = int(input())
    # 打印答案
    print(''.join([chr(ord('A')+i) for i in range(k)]))

if __name__ == '__main__':
    main()