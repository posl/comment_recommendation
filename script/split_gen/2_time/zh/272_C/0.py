def main():
    n, m = map(int, input().split())
    x = [[0]*n for i in range(n)]
    for i in range(m):
        data = list(map(int, input().split()))
        for j in range(1, data[0]+1):
            for k in range(j+1, data[0]+1):
                x[data[j]-1][data[k]-1] = 1
                x[data[k]-1][data[j]-1] = 1
    for i in range(n):
        for j in range(i+1, n):
            if x[i][j] == 0:
                print("No")
                return
    print("Yes")
    return
