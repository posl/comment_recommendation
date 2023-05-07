def main():
    n,k = map(int,input().split())
    p = [list(map(int,input().split())) for i in range(n)]
    p = sorted(p,key=lambda x:sum(x),reverse=True)
    for i in range(n):
        if p[i][0]+p[i][1]+p[i][2] < p[k-1][0]+p[k-1][1]+p[k-1][2]:
            print("No")
        else:
            print("Yes")
