def main():
    import math
    n = int(input())
    x = []
    y = []
    for _ in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    max_len = 0
    for i in range(n):
        for j in range(i + 1, n):
            max_len = max(max_len, math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2))
    print(max_len)
main()
