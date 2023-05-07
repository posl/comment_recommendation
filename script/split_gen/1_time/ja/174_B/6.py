def main():
    N,D=map(int,input().split())
    ans=0
    for i in range(N):
        x,y=map(int,input().split())
        if (x**2+y**2)**(1/2)<=D:
            ans+=1
    print(ans)
