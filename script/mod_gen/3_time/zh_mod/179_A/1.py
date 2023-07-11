def main():
    # 读入
    S = input()
    # 处理
    if S[-1] == 's':
        S += 'es'
    else:
        S += 's'
    # 输出
    print(S)

if __name__ == '__main__':
    main()