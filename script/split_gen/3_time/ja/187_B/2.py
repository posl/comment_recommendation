def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    count = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if y[i] - y[j] <= (x[i] - x[j]) * 1 and y[i] - y[j] >= (x[i] - x[j]) * (-1):
                count += 1
    print(count)
