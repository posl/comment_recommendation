def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_,y_ = map(int,input().split())
        x.append(x_)
        y.append(y_)
    s = input()
    x_ = [0]*n
    y_ = [0]*n
    for i in range(n):
        if s[i] == 'R':
            x_[i] = 1
        else:
            x_[i] = -1
    for i in range(n):
        if s[i] == 'U':
            y_[i] = 1
        else:
            y_[i] = -1
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0
    for i in range(n):
        if x[i]+x_[i] < x_min:
            x_min = x[i]+x_[i]
        if x[i]+x_[i] > x_max:
            x_max = x[i]+x_[i]
        if y[i]+y_[i] < y_min:
            y_min = y[i]+y_[i]
        if y[i]+y_[i] > y_max:
            y_max = y[i]+y_[i]
    if x_min < x_max and y_min < y_max:
        print('Yes')
    else:
        print('No')
