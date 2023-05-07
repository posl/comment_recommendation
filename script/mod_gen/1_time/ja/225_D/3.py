def main():
    n,q=map(int,input().split())
    trains=[i for i in range(n+1)]
    for i in range(q):
        query=list(map(int,input().split()))
        if query[0]==1:
            trains[query[2]]=trains[query[1]]
        elif query[0]==2:
            trains[query[2]]=query[2]
        else:
            ans=[]
            for j in range(1,n+1):
                if trains[j]==query[1]:
                    ans.append(j)
            print(len(ans),*ans)
    
    return 0

if __name__ == '__main__':
    main()