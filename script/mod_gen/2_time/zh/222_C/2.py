def f(a,b):
    if a == "G" and b == "C":
        return 1
    elif a == "C" and b == "P":
        return 1
    elif a == "P" and b == "G":
        return 1
    elif a == b:
        return 0
    else:
        return -1
n,m = map(int,input().split())
a = []
for i in range(2*n):
    a.append(input())
rank = [[i+1,0] for i in range(2*n)]
for i in range(m):
    for j in range(n):
        if f(a[rank[2*j][0]-1][i],a[rank[2*j+1][0]-1][i]) == 1:
            rank[2*j][1] += 1
        elif f(a[rank[2*j][0]-1][i],a[rank[2*j+1][0]-1][i]) == -1:
            rank[2*j+1][1] += 1
rank.sort(key=lambda x:x[1],reverse=True)
for i in range(2*n):
    print(rank[i][0])

if __name__ == '__main__':
    f()