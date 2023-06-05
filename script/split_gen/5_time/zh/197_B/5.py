def main():
    h,w,x,y=map(int,input().split())
    s=[input() for _ in range(h)]
    x-=1
    y-=1
    ans=1
    for i in range(x-1,-1,-1):
        if s[i][y]=='#':
            break
        ans+=1
    for i in range(x+1,h):
        if s[i][y]=='#':
            break
        ans+=1
    for i in range(y-1,-1,-1):
        if s[x][i]=='#':
            break
        ans+=1
    for i in range(y+1,w):
        if s[x][i]=='#':
            break
        ans+=1
    print(ans)
