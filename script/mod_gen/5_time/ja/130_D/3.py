def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    #print(N)
    #print(K)
    #print(A)
    #print(len(A))
    for i in range(N):
        #print("i:" + str(i))
        for j in range(i, N):
            #print("j:" + str(j))
            #print(A[i:j+1])
            if sum(A[i:j+1]) >= K:
                #print("sum:" + str(sum(A[i:j+1])))
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()