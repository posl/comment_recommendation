def xor(a,b):
    if a%4==0:
        return b
    elif a%4==1:
        return 1
    elif a%4==2:
        return b+1
    else:
        return 0
a,b=map(int,input().split())
print(xor(a-1,b))
