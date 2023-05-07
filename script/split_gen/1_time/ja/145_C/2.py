def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_, y_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
    print(x)
    print(y)
