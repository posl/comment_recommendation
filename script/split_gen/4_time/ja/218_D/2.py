def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    x.sort()
    y.sort()
    dx = [x[i+1] - x[i] for i in range(N-1)]
    dy = [y[i+1] - y[i] for i in range(N-1)]
    dx.sort()
    dy.sort()
    print(dx.count(dx[-1]) * dy.count(dy[-1]))
