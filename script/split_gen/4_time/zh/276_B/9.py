def main():
    n,m = map(int,input().split())
    d = [0 for i in range(n)]
    a = [[] for i in range(n)]
    for i in range(m):
        a1,a2 = map(int,input().split())
        a1 -= 1
        a2 -= 1
        a[a1].append(a2)
        a[a2].append(a1)
        d[a1] += 1
        d[a2] += 1
    for i in range(n):
        print(d[i],end=' ')
        for j in range(d[i]):
            print(a[i][j]+1,end=' ')
        print()
