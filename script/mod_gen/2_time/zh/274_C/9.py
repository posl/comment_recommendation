def main():
    N = int(input())
    A = list(map(int, input().split()))
    #生成距离
    d = [0]*(2*N+1)
    #变形虫1与变形虫1是零代的关系。
    d[1] = 0
    #变形虫2与变形虫1有一代之隔。
    d[2] = 1
    #变形虫3与变形虫1相距一代。
    d[3] = 1
    #变形虫4与变形虫2相距一代，与变形虫1相距两代。
    d[4] = 2
    #变形虫5与变形虫2相距一代，与变形虫1相距两代。
    d[5] = 2
    for i in range(1, N):
        #变形虫A_i与变形虫1相距一代。
        d[2*i] = 1
        #变形虫A_i与变形虫1相距一代。
        d[2*i+1] = 1
        #变形虫A_i与变形虫1相距一代。
        d[A[i-1]] = 1
    for i in range(1, N+1):
        for j in range(2*i, 2*N+1, i):
            d[j] = d[i]+1
    for i in range(1, 2*N+1):
        print(d[i])

if __name__ == '__main__':
    main()