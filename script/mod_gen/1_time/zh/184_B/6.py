def main():
    n,x=map(int,input().split())
    s=input()
    sum=x
    for i in range(n):
        if s[i]=="o":
            sum+=1
        else:
            if sum>0:
                sum-=1
    print(sum)
main()
