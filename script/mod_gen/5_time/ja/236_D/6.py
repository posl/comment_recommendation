def solve():
    #n = int(input())
    #a = list(map(int, input().split()))
    #b = list(map(int, input().split()))
    #c = list(map(int, input().split()))
    #s = input()
    n=int(input())
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    ans=0
    for i in range(2**n):
        flag=True
        for j in range(n):
            for k in range(j+1,n):
                if i>>j&i>>k&1 and a[j][k]==1:
                    flag=False
        if flag:
            cnt=0
            for j in range(n):
                if i>>j&1:
                    cnt+=1
            ans=max(ans,cnt)
    print(ans)
    #print(*ans,sep='\n')

if __name__ == '__main__':
    solve()