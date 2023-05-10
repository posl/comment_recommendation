def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    
    B = [0] * (2*N+2)
    for i in range(1, N+1):
        B[i] = A[i]
        B[i*2] = A[i]
        B[i*2+1] = A[i]
    
    #print(B)
    
    for i in range(1, 2*N+2):
        cnt = 0
        while B[i] != 1:
            #print(B[i])
            B[i] = B[int(B[i]/2)]
            cnt += 1
        print(cnt)

if __name__ == '__main__':
    main()