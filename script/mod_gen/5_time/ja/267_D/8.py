def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    #print(N,M,A)
    #Bの部分列を求める
    #Bの長さでループ
    B = []
    for i in range(M,N+1):
        #print("i:",i)
        #Bの開始位置でループ
        for j in range(0,N-i+1):
            #print("j:",j)
            #Bの部分列を作る
            #print(A[j:j+i])
            B.append(A[j:j+i])
    #print(B)
    #Bの部分列の和の最大値を求める
    ans = -10**9
    for b in B:
        #print("b:",b)
        s = 0
        for i in range(1,len(b)+1):
            s += i*b[i-1]
        #print("s:",s)
        ans = max(ans,s)
    print(ans)

if __name__ == '__main__':
    main()