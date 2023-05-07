def main():
    A,B,C=map(int,input().split())
    ans=0
    for i in range(100):
        ans+=1
        for j in range(3):
            if i==99:
                ans+=100
                break
            if j==0:
                ans+=(A/(A+B+C))
                A+=A
            elif j==1:
                ans+=(B/(A+B+C))
                B+=B
            elif j==2:
                ans+=(C/(A+B+C))
                C+=C
    print(ans)

if __name__ == '__main__':
    main()