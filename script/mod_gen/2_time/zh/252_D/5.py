def main():
    N=int(input())
    A=list(map(int,input().split()))
    A.sort()
    #print(A)
    ans=0
    for i in range(N-2):
        for j in range(i+1,N-1):
            if A[i]==A[j]:
                continue
            for k in range(j+1,N):
                if A[i]==A[k] or A[j]==A[k]:
                    continue
                ans+=1
    print(ans)

if __name__ == '__main__':
    main()