def main():
    n=int(input())
    a=list(map(int,input().split()))
    a.insert(0,0)
    b=[0]*(2*n+1)
    for i in range(1,n+1):
        b[i]=1
    for i in range(n,0,-1):
        b[i]=b[i*2]+1
        b[i]=b[i*2+1]+1
    for i in range(1,2*n+1):
        print(b[i])
