def main():
    n,m,c = map(int,input().split())
    b = list(map(int,input().split()))
    a = [list(map(int,input().split())) for i in range(n)]
    cnt = 0
    for i in range(n):
        sum = c
        for j in range(m):
            sum += a[i][j]*b[j]
        if sum > 0:
            cnt += 1
    print(cnt)
