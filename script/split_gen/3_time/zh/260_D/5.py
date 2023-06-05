def main():
    n,k = map(int, input().split())
    p = list(map(int, input().split()))
    x = [0]*(n+1)
    y = [0]*(n+1)
    for i in range(n):
        x[p[i]] = i+1
    for i in range(n):
        y[i+1] = x[i+1]
    for i in range(n):
        if y[i+1] == 0:
            print(-1)
        else:
            print(y[i+1])
        if i >= k-1:
            y[p[i-k+1]] = 0
