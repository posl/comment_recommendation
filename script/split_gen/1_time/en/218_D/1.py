def main():
    n = int(input())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j]:
                continue
            for k in range(j + 1, n):
                if x[i] == x[k] or y[i] == y[k]:
                    continue
                if x[i] == x[j] or y[i] == y[j]:
                    continue
                if (x[i] - x[j]) * (y[i] - y[k]) == (x[i] - x[k]) * (y[i] - y[j]):
                    count += 1
    print(count)
main()
