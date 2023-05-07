def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    #累積和を求める
    cumsum = [0]
    for i in range(N):
        cumsum.append(cumsum[i]+A[i])
    #すべてのx,yについて、累積和の差を求める
    ans = 10**9
    for x in range(N+1):
        for y in range(N+1):
            if x+y > N:
                break
            #累積和の差を求める
            diff = cumsum[N]-cumsum[N-y]-cumsum[x]
            #x,yの操作の結果
            #xが0の場合は、A_1,A_2,...,A_N
            #yが0の場合は、A_{N},A_{N-1},...,A_{N-y+1}
            #それ以外の場合は、A_1,A_2,...,A_x,L,A_{N},A_{N-1},...,A_{N-y+1},R
            if x == 0:
                if y == 0:
                    #x,yともに0の場合は、A_1,A_2,...,A_N
                    #何もしないので、diffはそのまま
                    pass
                else:
                    #xが0,yが0以外の場合は、A_1,A_2,...,A_N,R
                    #yの個数分、Rを引く
                    diff -= R*y
            else:
                if y == 0:
                    #xが0以外,yが0の場合は、A_1,A_2,...,A_x,L
                    #xの個数分、Lを足す
                    diff += L*x
                else:
                    #x,yともに0以外の場合は、A_1,A_2,...,A_x,L,A_{N},A_{N-1},...,A_{N-y+1},R
                    #xの個数分、Lを足す
                    diff += L*x
                    #yの

if __name__ == '__main__':
    main()