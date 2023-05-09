def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_, y_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
    x.sort()
    y.sort()
    x_ = []
    y_ = []
    for i in range(n-1):
        x_.append(x[i+1] - x[i])
        y_.append(y[i+1] - y[i])
    x_.sort()
    y_.sort()
    print(x_.count(x_[0]) * y_.count(y_[0]))
main()
