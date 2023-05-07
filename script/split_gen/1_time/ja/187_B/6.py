def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if (y[j] - y[i]) / (x[j] - x[i]) <= 1 and (y[j] - y[i]) / (x[j] - x[i]) >= -1:
                count += 1
    print(count)
