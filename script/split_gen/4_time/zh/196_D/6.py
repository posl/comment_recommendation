def cal(a,b):
    if a == 0:
        return 1
    elif a == 1:
        return b
    elif a > b:
        return 0
    else:
        return cal(a,b-1) + cal(a-1,b-1)
    
h,w,a,b = map(int,input().split())
print(cal(a,b)*cal(a,h-b)*cal(w-a,b)*cal(w-a,h-b))
