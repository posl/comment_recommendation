def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    #print(n,k,a)
    max=0
    for i in range(0,k+1):
        sum=0
        for j in range(0,n):
            sum+=i^a[j]
        if sum>max:
            max=sum
    print(max)
