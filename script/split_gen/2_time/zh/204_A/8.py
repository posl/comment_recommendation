def main():
    n,k = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(n)]
    #a = [[1,7,0],[5,8,11],[10,4,2]]
    #a = [[1,2,3],[4,5,6],[7,8,9]]
    #print(a)
    ans = 10**9
    for i in range(n-k+1):
        for j in range(n-k+1):
            #print(i,j)
            b = []
            for x in range(i,i+k):
                for y in range(j,j+k):
                    b.append(a[x][y])
            b.sort()
            #print(b)
            ans = min(ans,b[(k**2)//2])
    print(ans)
