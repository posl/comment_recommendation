def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x1, y1 = map(int, input().split())
        x.append(x1)
        y.append(y1)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans = max(ans, ((x[i] - x[j])**2 + (y[i] - y[j])**2)**0.5)
    print(ans)
