def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans = max(ans, (x[i]-x[j])**2+(y[i]-y[j])**2)
    print(ans**0.5)
