def main():
    # 输入
    S = input()
    # 逻辑
    count = 0
    for i in range(4):
        if S[i] == '+':
            count += 1
        else:
            count -= 1
    # 输出
    print(count)

if __name__ == '__main__':
    main()