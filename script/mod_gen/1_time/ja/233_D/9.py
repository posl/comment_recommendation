def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, A)
    #print(sum(A))
    #print(sum(A[1:2]))
    #print(sum(A[1:3]))
    #print(sum(A[1:4]))
    #print(sum(A[1:5]))
    #print(sum(A[1:6]))
    #print(sum(A[2:3]))
    #print(sum(A[2:4]))
    #print(sum(A[2:5]))
    #print(sum(A[2:6]))
    #print(sum(A[3:4]))
    #print(sum(A[3:5]))
    #print(sum(A[3:6]))
    #print(sum(A[4:5]))
    #print(sum(A[4:6]))
    #print(sum(A[5:6]))
    
    count = 0
    for i in range(N):
        for j in range(i+1, N+1):
            if sum(A[i:j]) == K:
                count += 1
    print(count)

if __name__ == '__main__':
    main()