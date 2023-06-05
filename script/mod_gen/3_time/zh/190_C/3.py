def main():
    # 读入数据
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    K = int(input())
    C = []
    D = []
    for i in range(K):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    # 遍历所有可能的状态
    ans = 0
    for i in range(2 ** K):
        dish = [False] * N
        for j in range(K):
            if (i >> j) & 1:
                dish[C[j]-1] = True
            else:
                dish[D[j]-1] = True
        cnt = 0
        for j in range(M):
            if dish[A[j]-1] and dish[B[j]-1]:
                cnt += 1
        if ans < cnt:
            ans = cnt
    print(ans)

if __name__ == '__main__':
    main()