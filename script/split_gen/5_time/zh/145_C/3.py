def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    import itertools
    total = 0
    for i in itertools.permutations(range(N)):
        for j in range(N - 1):
            total += ((x[i[j]] - x[i[j + 1]]) ** 2 + (y[i[j]] - y[i[j + 1]]) ** 2) ** 0.5
    print(total / (N - 1))
