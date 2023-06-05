def main():
    n,d=map(int,input().split())
    l=[]
    for i in range(n):
        l.append(list(map(int,input().split())))
    l.sort(key=lambda x:x[0])
    count=1
    for i in range(n-1):
        if l[i][1]>l[i+1][0]:
            count+=1
    print(count)
