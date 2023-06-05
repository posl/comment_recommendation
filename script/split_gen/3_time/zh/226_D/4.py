def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i,y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
    x.sort()
    y.sort()
    #print(x)
    #print(y)
    x_min = x[0]
    x_max = x[N-1]
    y_min = y[0]
    y_max = y[N-1]
    #print(x_min)
    #print(x_max)
    #print(y_min)
    #print(y_max)
    x_min_x_max = x_max-x_min
    y_min_y_max = y_max-y_min
    #print(x_min_x_max)
    #print(y_min_y_max)
    if x_min_x_max > y_min_y_max :
        print(x_min_x_max)
    else:
        print(y_min_y_max)
