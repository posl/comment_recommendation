def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    x.sort()
    y.sort()
    #print(x)
    #print(y)
    if N % 2 == 0:
        min_x = (x[N//2-1] + x[N//2]) // 2
        max_x = min_x + 1
        min_y = (y[N//2-1] + y[N//2]) // 2
        max_y = min_y + 1
        #print(min_x, max_x, min_y, max_y)
        ans = (max_x - min_x + 1) * (max_y - min_y + 1)
    else:
        min_x = x[N//2]
        max_x = min_x
        min_y = y[N//2]
        max_y = min_y
        #print(min_x, max_x, min_y, max_y)
        ans = 1
    print(ans)
