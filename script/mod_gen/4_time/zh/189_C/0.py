def main():
    #输入
    N = int(input())
    A = list(map(int, input().split()))
    #计算
    max_orange = 0
    for l in range(N):
        for r in range(l, N):
            x = min(A[l:r+1])
            max_orange = max(max_orange, x*(r-l+1))
    #输出
    print(max_orange)

if __name__ == '__main__':
    main()