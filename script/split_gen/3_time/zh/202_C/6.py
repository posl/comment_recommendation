def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    count=[0]*n
    for i in range(n):
        count[b[c[i]-1]-1]+=1
    ans=0
    for i in range(n):
        ans+=count[a[i]-1]
    print(ans)
