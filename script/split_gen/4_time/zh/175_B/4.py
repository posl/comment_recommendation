def getnum(n):
    n.sort()
    num=0
    for i in range(len(n)-2):
        for j in range(i+1,len(n)-1):
            for k in range(j+1,len(n)):
                if n[i]+n[j]>n[k]:
                    num+=1
    return num
n=int(input())
a=list(map(int,input().split()))
print(getnum(a))
