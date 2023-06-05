def main():
    # 读取输入
    S = input()
    # 初始化
    ans = 0
    # 吃符号
    for i in range(len(S)):
        if S[i] == '+':
            ans += 1
        elif S[i] == '-':
            ans -= 1
        else:
            pass
    # 输出答案
    print(ans)

if __name__ == '__main__':
    main()