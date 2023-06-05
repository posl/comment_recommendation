def main():
    # 读取输入
    N = int(input())
    S = input()
    # print('N=', N)
    # print('S=', S)
    # 统计粘液数量
    slime_count = 1
    for i in range(1, N):
        if S[i] != S[i-1]:
            slime_count += 1
    # 输出结果
    print(slime_count)

if __name__ == '__main__':
    main()