def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_y = input().split()
        x.append(int(x_y[0]))
        y.append(int(x_y[1]))
    # print(x)
    # print(y)
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if (y[i]-y[j])/(x[i]-x[j]) >= -1 and (y[i]-y[j])/(x[i]-x[j]) <= 1:
                ans += 1
    print(ans)
