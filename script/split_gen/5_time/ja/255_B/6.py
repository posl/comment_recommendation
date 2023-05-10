def main():
    import sys
    n,k = map(int,sys.stdin.readline().split())
    a = list(map(int,sys.stdin.readline().split()))
    xy = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    x = [xy[i][0] for i in range(n)]
    y = [xy[i][1] for i in range(n)]
    x.sort()
    y.sort()
    #print(x)
    #print(y)
    #print(a)
    #xの中央値
    if n%2 == 0:
        x_med = (x[n//2-1]+x[n//2])/2
    else:
        x_med = x[n//2]
    #yの中央値
    if n%2 == 0:
        y_med = (y[n//2-1]+y[n//2])/2
    else:
        y_med = y[n//2]
    #print(x_med)
    #print(y_med)
    #中央値からの距離の最大値
    x_max = max([abs(x[i]-x_med) for i in range(n)])
    y_max = max([abs(y[i]-y_med) for i in range(n)])
    #print(x_max)
    #print(y_max)
    #中央値からの距離の最大値が答え
    print(max(x_max,y_max))
