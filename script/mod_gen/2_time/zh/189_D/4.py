def main():
    N=int(input())
    S=[]
    for i in range(N):
        S.append(input())
    #print(N)
    #print(S)
    ans=0
    for i in range(N):
        if S[i]=="OR":
            ans+=2**(i+1)
    ans+=1
    print(ans)

if __name__ == '__main__':
    main()