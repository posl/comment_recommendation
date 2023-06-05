def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    for i in range(n):
        b.append(0)
    for i in range(n):
        b[a[i]-1]+=1
    for i in range(n):
        if b[i]==0:
            print(0)
            continue
        elif b[i]==1:
            print(1)
            continue
        else:
            if b[i]%2==0:
                print(0)
            else:
                print(1)
main()
