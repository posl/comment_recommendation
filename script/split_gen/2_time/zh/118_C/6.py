def main():
    n,m = map(int,input().split())
    k = []
    a = []
    for i in range(n):
        k.append(list(map(int,input().split())))
        a.append(list(map(int,input().split())))
    food = [0]*m
    for i in range(n):
        for j in range(k[i][0]):
            food[a[i][j]-1] += 1
    count = 0
    for i in range(m):
        if food[i] == n:
            count += 1
    print(count)
