def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if (y[j] - y[i]) / (x[j] - x[i]) <= 1 and (y[j] - y[i]) / (x[j] - x[i]) >= -1:
                count += 1
    print(count)
