def main():
    #N
    N = int(input())
    #P_1 ... P_N
    P = list(map(int, input().split()))
    #P_i ≦ P_j
    #i(1 ≦ i ≦ N) の個数
    count = 0
    #任意の整数 j(1 ≦ j ≦ i) に対して、 P_i ≦ P_j
    #i=1,2,3,4,...,N
    for i in range(N):
        #j=1,2,3,4,...,i
        for j in range(i+1):
            #P_i ≦ P_j
            if P[i] <= P[j]:
                #i(1 ≦ i ≦ N) の個数
                count += 1
                break
    #条件を満たす整数 i の個数
    print(count)

if __name__ == '__main__':
    main()