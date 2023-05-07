def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if -1 <= (y[j]-y[i])/(x[j]-x[i]) <= 1:
                ans += 1
    print(ans)
