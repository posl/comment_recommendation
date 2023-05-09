def xor(a,b):
    if a==b:
        return a
    elif a==0:
        return b
    elif b==0:
        return a
    elif a==1:
        if b==2:
            return 3
        elif b==3:
            return 2
        elif b==1:
            return 0
        elif b==0:
            return 1
    elif a==2:
        if b==1:
            return 3
        elif b==3:
            return 1
        elif b==0:
            return 2
    elif a==3:
        if b==1:
            return 2
        elif b==2:
            return 1
        elif b==0:
            return 3
a,b=map(int,input().split())
ans=0
for i in range(a,b+1):
    ans=xor(ans,i)
print(ans)

if __name__ == '__main__':
    xor()