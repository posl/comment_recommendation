def main():
    # 读取输入
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    # 从最后一个字符串开始，逐个向前检查是否有重叠
    for i in range(M-1, -1, -1):
        # 检查T[i]是否与S中的任何一个字符串重叠
        for j in range(N):
            # 如果重叠，就将T[i]从S中删除
            if T[i] in S[j]:
                S.remove(T[i])
                break
    # 从最后一个字符串开始，逐个向前检查是否有重叠
    for i in range(M-1, -1, -1):
        # 检查T[i]是否与S中的任何一个字符串重叠
        for j in range(N):
            # 如果重叠，就将T[i]从S中删除
            if T[i] in S[j]:
                S.remove(T[i])
                break
    # 如果没有重叠的字符串，就输出-1
    if len(S) == 0:
        print(-1)
        return
    # 如果有重叠的字符串，就将它们按长度从大到小排序
    S.sort(key=len, reverse=True)
    # 将所有字符串连接起来
    ans = ''.join(S)
    # 将_替换为新的字符串
    print(ans.replace('_', ''))

if __name__ == '__main__':
    main()