def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    
    A.sort()
    B.sort()
    B.reverse()
    
    #print(A)
    #print(B)
    
    for i in range(N):
        if abs(A[i]-B[i]) > K:
            print("No")
            exit()
    
    print("Yes")
    
main()

if __name__ == '__main__':
    main()