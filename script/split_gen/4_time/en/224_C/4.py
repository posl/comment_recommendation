def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (x[j]-x[i])*(y[k]-y[i]) != (x[k]-x[i])*(y[j]-y[i]):
                    count += 1
    print(count)
