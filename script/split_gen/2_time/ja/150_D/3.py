def main():
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    LCM=1
    for a in A:
        LCM=LCM*a//gcd(LCM,a)
    ans=0
    for a in A:
        ans+=M//LCM*(LCM//a)
        if LCM//a%2==1:
            ans+=max(0,M%LCM-(LCM//a-1)//2)
    print(ans)
