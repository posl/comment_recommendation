def main():
    import math
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    max = 0
    for i in range(N):
        for j in range(i+1,N):
            tmp = math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
            if tmp > max:
                max = tmp
    print(max)
    return 0
