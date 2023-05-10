def main():
    N=int(input())
    flag=False
    count=0
    for i in range(N):
        a,b=map(int,input().split())
        if a==b:
            count+=1
            if count>=3:
                flag=True
        else:
            count=0
    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()