def main():
    # 读取输入
    S = input()
    # 处理
    S = S[1:] + S[0]
    # 输出
    print(S)

if __name__ == '__main__':
    main()