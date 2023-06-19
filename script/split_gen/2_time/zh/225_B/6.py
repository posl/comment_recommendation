def main():
    N=int(input())
    edges=[]
    for i in range(N-1):
        a,b=map(int,input().split())
        edges.append((a,b))
    edges.sort()
    cnt=[0]*(N+1)
    for e in edges:
        cnt[e[0]]+=1
        cnt[e[1]]+=1
    for i in range(1,N+1):
        if cnt[i]==N-1:
            print("Yes")
            return
    print("No")
main()
