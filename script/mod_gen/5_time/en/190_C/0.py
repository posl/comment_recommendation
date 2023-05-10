def main():
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
    ans = 0
    for i in range(2**K):
        dish = [0]*N
        for j in range(K):
            if (i>>j)&1:
                dish[C[j]-1] += 1
            else:
                dish[D[j]-1] += 1
        count = 0
        for k in range(M):
            if dish[A[k]-1] > 0 and dish[B[k]-1] > 0:
                count += 1
        ans = max(ans, count)
    print(ans)

if __name__ == '__main__':
    main()