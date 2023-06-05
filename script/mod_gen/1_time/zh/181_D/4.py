def solve():
    # 读取输入
    S = input()
    # 从S中取出数字
    N = len(S)
    # 如果S中有一个数字是8的倍数，那么S就是8的倍数
    for i in range(N):
        if int(S[i]) % 8 == 0:
            print("是")
            return
    # 如果S中有两个数字是8的倍数，那么S就是8的倍数
    for i in range(N):
        for j in range(i + 1, N):
            if int(S[i] + S[j]) % 8 == 0 or int(S[j] + S[i]) % 8 == 0:
                print("是")
                return
    # 如果S中有三个数字是8的倍数，那么S就是8的倍数
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if int(S[i] + S[j] + S[k]) % 8 == 0 or int(S[i] + S[k] + S[j]) % 8 == 0 or int(S[j] + S[i] + S[k]) % 8 == 0 or int(S[j] + S[k] + S[i]) % 8 == 0 or int(S[k] + S[i] + S[j]) % 8 == 0 or int(S[k] + S[j] + S[i]) % 8 == 0:
                    print("是")
                    return
    # 如果S中有四个数字是8的倍数，那么S就是8的倍数
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                for l in range(k + 1, N):
                    if int(S[i] + S[j] + S[k] + S[l]) % 8 == 0 or int(S[i] + S[j] + S[l] + S[k]) % 8 == 0 or int(S[i] + S[k] + S[j] + S[l]) % 8 == 0 or int(S[i] + S[k] + S[l

if __name__ == '__main__':
    solve()