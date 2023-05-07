def main():
    N,M=map(int,input().split())
    edge=[[] for _ in range(N)]
    for _ in range(M):
        a,b=map(int,input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    ans="Yes"
    for i in range(N):
        if len(edge[i])%2==1:
            ans="No"
    print(ans)

if __name__ == '__main__':
    main()