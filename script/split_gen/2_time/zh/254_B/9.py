def main():
    n=int(input())
    a=[[1]*n for i in range(n)]
    for i in range(n):
        for j in range(1,i):
            a[i][j]=a[i-1][j-1]+a[i-1][j]
    for i in range(n):
        print(" ".join(map(str,a[i][:i+1])))
