def a165(k,a,b):
    if a%k==0 or b%k==0:
        print('OK')
    elif a//k==b//k:
        print('NG')
    else:
        print('OK')
k=int(input())
a,b=map(int,input().split())
a165(k,a,b)
