def main():
    # 将输入的字符串转换为列表
    N, Q = map(int, input().split())
    S = list(input())
    # 依次处理Q个查询
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            # 1 x:连续执行以下x次：删除S的最后一个字符并将其附加到开头。
            S = S[-x:] + S[:-x]
        else:
            # 2 x:打印S的第x个字符。
            print(S[x - 1])

if __name__ == '__main__':
    main()