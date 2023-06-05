def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_, y_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (x[i]-x[k])*(y[j]-y[k]) != (x[j]-x[k])*(y[i]-y[k]):
                    ans += 1
    print(ans)
