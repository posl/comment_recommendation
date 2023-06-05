def main():
    # 输入
    S = input()
    # 反转
    S = S[::-1]
    # 替换
    S = S.replace('6', 't')
    S = S.replace('9', '6')
    S = S.replace('t', '9')
    S = S.replace('0', 't')
    S = S.replace('1', '0')
    S = S.replace('t', '1')
    # 输出
    print(S)

if __name__ == '__main__':
    main()