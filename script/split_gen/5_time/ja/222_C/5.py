def check(a,b):
    if a == "G" and b == "C":
        return True
    elif a == "C" and b == "P":
        return True
    elif a == "P" and b == "G":
        return True
    else:
        return False
n,m = map(int,input().split())
a = []
for i in range(2*n):
    a.append(input())
rank = []
for i in range(2*n):
    rank.append([0,i+1])
for i in range(m):
    for j in range(n):
        if check(a[rank[2*j][1]-1][i],a[rank[2*j+1][1]-1][i]):
            rank[2*j][0] -= 1
        elif check(a[rank[2*j+1][1]-1][i],a[rank[2*j][1]-1][i]):
            rank[2*j+1][0] -= 1
rank.sort()
for i in range(2*n):
    print(rank[i][1])
