def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans = max(ans, (x[i] - x[j])**2 + (y[i] - y[j])**2)
    print(ans**0.5)
