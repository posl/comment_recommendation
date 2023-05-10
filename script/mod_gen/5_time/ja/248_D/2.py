def main():
    N=int(input())
    A=list(map(int,input().split()))
    Q=int(input())
    A_list = [0]*(N+1)
    for i in range(N):
        A_list[A[i]]+=1
    ans = 0
    for i in range(Q):
        L,R,X=map(int,input().split())
        ans = 0
        for j in range(L,R+1):
            if A[j-1]==X:
                ans+=1
        print(ans)

if __name__ == '__main__':
    main()