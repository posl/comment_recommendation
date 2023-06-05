def main():
    # 读取输入
    N, M = map(int, input().split())
    S = []
    T = []
    for i in range(N):
        S.append(input())
    for i in range(M):
        T.append(input())
    # 从S中找到最长的字符串
    max_len = 0
    for i in range(N):
        if len(S[i]) > max_len:
            max_len = len(S[i])
    # 从T中找到最长的字符串
    for i in range(M):
        if len(T[i]) > max_len:
            max_len = len(T[i])
    # 从S中找到最长的字符串
    for i in range(N):
        if len(S[i]) > max_len:
            max_len = len(S[i])
    # 从S中找到最长的字符串
    for i in range(N):
        if len(S[i]) > max_len:
            max_len = len(S[i])
    # 从S中找到最长的字符串
    for i in range(N):
        if len(S[i]) > max_len:
            max_len = len(S[i])
    # 从S中找到最长的字符串
    for i in range(N):
        if len(S[i]) > max_len:
            max_len = len(S[i])
    # 从S中找到最长的字符串
    for i in range(N):
        if len(S[i]) > max_len:
            max_len = len(S[i])
    # 从S中找到最长的字符串
    for i in range(N):
        if len(S[i]) > max_len:
            max_len = len(S[i])
    # 从S中找到最长的字符串
    for i in range(N):
        if len(S[i]) > max_len:
            max_len = len(S[i])
    # 从S中找到最长的字符串
    for i in range(N):
        if len(S[i]) > max_len:
            max_len = len(S[i])
    print(max_len)

if __name__ == '__main__':
    main()