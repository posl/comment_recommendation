def main():
    n,k=map(int,input().split())
    a=[]
    for i in range(k):
        a.append(list(map(int,input().split())))
    #print(a)
    b=[0 for i in range(n)]
    #print(b)
    for i in range(k):
        for j in range(len(a[i])):
            b[a[i][j]-1]+=1
    #print(b)
    count=0
    for i in range(n):
        if b[i]==0:
            count+=1
    print(count)
main()
