def main():
    n = int(input())
    x = [0]*n
    y = [0]*n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    x.sort()
    y.sort()
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            ans += (x[j]-x[i])*(y[j]-y[i])
    print(ans)
