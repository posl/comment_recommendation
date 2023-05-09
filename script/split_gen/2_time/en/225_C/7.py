def solve(n,m,b):
    for i in range(1,n+1):
        for j in range(1,m+1):
            if (i-1)*m+j != b[i-1][j-1]:
                return "No"
    return "Yes"
n,m = map(int,input().split())
b = []
for i in range(n):
    b.append(list(map(int,input().split())))
print(solve(n,m,b))
