def main():
    n, m = map(int, input().split())
    a = [[0]*n for _ in range(n)]
    for _ in range(m):
        k, *x = map(int, input().split())
        for i in range(k):
            for j in range(i+1,k):
                a[x[i]-1][x[j]-1] = 1
                a[x[j]-1][x[i]-1] = 1
    for i in range(n):
        if sum(a[i]) != n-1:
            print("No")
            exit()
    print("Yes")
