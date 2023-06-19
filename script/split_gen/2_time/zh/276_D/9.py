def main():
    n=int(input())
    A=list(map(int,input().split()))
    count=0
    while True:
        flag=0
        for i in range(n):
            if A[i]%2==0:
                A[i]=A[i]/2
                flag=1
            if A[i]%3==2:
                A[i]=A[i]/3
                flag=1
        if flag==1:
            count+=1
        else:
            break
    for i in range(1,n):
        if A[i]!=A[0]:
            count=-1
            break
    print(count)
    
main()
