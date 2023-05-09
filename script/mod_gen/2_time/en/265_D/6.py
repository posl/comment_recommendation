def main():
    #input
    N,P,Q,R=map(int,input().split())
    A=list(map(int,input().split()))
    #solve
    ans="No"
    for i in range(N-3):
        for j in range(i+1,N-2):
            for k in range(j+1,N-1):
                if P*A[i]+Q*A[j]+R*A[k]==P*max(A[:i])+Q*max(A[i:j])+R*max(A[j:k]):
                    ans="Yes"
                    break
    #output
    print(ans)

if __name__ == '__main__':
    main()