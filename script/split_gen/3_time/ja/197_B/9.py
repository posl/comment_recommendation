def check(x,y):
    if (x<0) or (x>=h) or (y<0) or (y>=w):
        return False
    if s[x][y] == "#":
        return False
    return True
h,w,x,y=map(int,input().split())
s=[list(input()) for _ in range(h)]
x-=1
y-=1
ans=1
for i in range(x-1,-1,-1):
    if check(i,y):
        ans+=1
    else:
        break
for i in range(x+1,h):
    if check(i,y):
        ans+=1
    else:
        break
for i in range(y-1,-1,-1):
    if check(x,i):
        ans+=1
    else:
        break
for i in range(y+1,w):
    if check(x,i):
        ans+=1
    else:
        break
print(ans)
