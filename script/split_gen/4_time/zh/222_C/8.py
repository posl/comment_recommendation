def main():
    n,m=map(int,input().split())
    a=[]
    for i in range(2*n):
        a.append(input())
    rank=[[i+1,0] for i in range(2*n)]
    for i in range(m):
        for j in range(n):
            if a[rank[2*j][0]-1][i]==a[rank[2*j+1][0]-1][i]:
                continue
            elif a[rank[2*j][0]-1][i]=="G" and a[rank[2*j+1][0]-1][i]=="C":
                rank[2*j][1]+=1
            elif a[rank[2*j][0]-1][i]=="C" and a[rank[2*j+1][0]-1][i]=="P":
                rank[2*j][1]+=1
            elif a[rank[2*j][0]-1][i]=="P" and a[rank[2*j+1][0]-1][i]=="G":
                rank[2*j][1]+=1
            else:
                rank[2*j+1][1]+=1
        rank.sort(key=lambda x:(-x[1],x[0]))
    for i in range(2*n):
        print(rank[i][0])
main()
