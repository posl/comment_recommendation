def dfs(a,b,k):
    if a==0:
        return 'b'*b
    if b==0:
        return 'a'*a
    i=comb[a+b-1][b]
    if k<=i:
        return 'a'+dfs(a-1,b,k)
    else:
        return 'b'+dfs(a,b-1,k-i)
A,B,K=map(int,input().split())
comb=[[0 for i in range(B+1)] for j in range(A+B+1)]
for i in range(A+B+1):
    comb[i][0]=1
    for j in range(1,min(i,B+1)):
        comb[i][j]=comb[i-1][j-1]+comb[i-1][j]
print(dfs(A,B,K))
