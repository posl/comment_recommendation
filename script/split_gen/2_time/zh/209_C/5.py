def solve(n,c):
    if n==1:
        return c[0]
    if n==2:
        return (c[0]+c[1])%1000000007
    if n==3:
        return (c[0]+c[1]+c[2])%1000000007
    if n==4:
        return (c[0]+c[1]+c[2]+c[3]+3)%1000000007
    if n==5:
        return (c[0]+c[1]+c[2]+c[3]+c[4]+6)%1000000007
    if n==6:
        return (c[0]+c[1]+c[2]+c[3]+c[4]+c[5]+10)%1000000007
    if n==7:
        return (c[0]+c[1]+c[2]+c[3]+c[4]+c[5]+c[6]+15)%1000000007
    if n==8:
        return (c[0]+c[1]+c[2]+c[3]+c[4]+c[5]+c[6]+c[7]+21)%1000000007
    if n==9:
        return (c[0]+c[1]+c[2]+c[3]+c[4]+c[5]+c[6]+c[7]+c[8]+28)%1000000007
    if n==10:
        return (c[0]+c[1]+c[2]+c[3]+c[4]+c[5]+c[6]+c[7]+c[8]+c[9]+36)%1000000007
n=int(input())
c=list(map(int,input().split()))
print(solve(n,c))
