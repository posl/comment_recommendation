def main():
    # 1. 读入数据
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    # 2. 枚举所有可能的字符串
    for i in range(3 ** N):
        # 3. 枚举第一项
        tmp = i
        X = ""
        for j in range(N):
            # 4. 枚举第j项
            X += S[j]
            if tmp % 3 == 0:
                X += "_"
            elif tmp % 3 == 1:
                X += "__"
            tmp //= 3
        # 5. 判断X是否满足条件
        ok = True
        for j in range(M):
            if T[j] in X:
                ok = False
        if ok:
            print(X)
            break
    else:
        print(-1)

if __name__ == '__main__':
    main()