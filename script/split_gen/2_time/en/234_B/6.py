def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    max_len = 0
    for i in range(n):
        for j in range(i + 1, n):
            max_len = max(max_len, (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
    print(max_len ** 0.5)
