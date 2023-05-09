def main():
    N = int(input())
    x, y = [], []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if (x[i]-x[j])*(y[j]-y[k]) == (x[j]-x[k])*(y[i]-y[j]):
                    print("Yes")
                    return
    print("No")
    return
