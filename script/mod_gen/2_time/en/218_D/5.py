def main():
    from collections import Counter
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    x_count = Counter(x)
    y_count = Counter(y)
    x_count = list(x_count.values())
    y_count = list(y_count.values())
    ans = 0
    for i in range(len(x_count)):
        for j in range(len(x_count)):
            if i == j:
                ans += x_count[i] * (x_count[j] - 1) // 2
            else:
                ans += x_count[i] * x_count[j]
    for i in range(len(y_count)):
        for j in range(len(y_count)):
            if i == j:
                ans += y_count[i] * (y_count[j] - 1) // 2
            else:
                ans += y_count[i] * y_count[j]
    print(ans)

if __name__ == '__main__':
    main()