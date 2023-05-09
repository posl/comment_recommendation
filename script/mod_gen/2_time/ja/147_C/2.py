def main():
    N = int(input())
    A = [0]*N
    x = [[] for i in range(N)]
    y = [[] for i in range(N)]
    for i in range(N):
        A[i] = int(input())
        for j in range(A[i]):
            x[i].append(0)
            y[i].append(0)
            x[i][j],y[i][j] = map(int,input().split())
    ans = 0
    for i in range(2**N):
        flg = True
        for j in range(N):
            if flg == False:
                break
            if ((i>>j)&1):
                for k in range(A[j]):
                    if y[j][k] == 1:
                        if ((i>>(x[j][k]-1))&1) == 0:
                            flg = False
                            break
                    else:
                        if ((i>>(x[j][k]-1))&1) == 1:
                            flg = False
                            break
        if flg:
            ans = max(ans,bin(i).count("1"))
    print(ans)

if __name__ == '__main__':
    main()