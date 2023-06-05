def cal(a):
    return a*(a-1)//2
n=int(input())
a=list(map(int,input().split()))
d={}
for i in range(n):
    if a[i] not in d:
        d[a[i]]=1
    else:
        d[a[i]]+=1
s=sum(list(map(cal,d.values())))
for i in range(n):
    print(s-(d[a[i]]-1))

if __name__ == '__main__':
    cal()