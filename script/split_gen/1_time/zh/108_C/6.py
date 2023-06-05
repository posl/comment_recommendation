def main():
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        if i%k==0:
            ans+=1
        elif (i*2)%k==0:
            ans+=1
        elif (i*3)%k==0:
            ans+=1
    print(ans)
